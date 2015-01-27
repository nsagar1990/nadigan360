from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, HttpRequest
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from models import *

import traceback
import json
from django.core import serializers

def render_response(request, template, data=None):
	data = data or {}  
    	r = RequestContext(request)
    	data['ref_path'] = request.get_full_path()
    	return render_to_response(template, data, context_instance=r)

def _get_http_response(message, status=200):
    	return HttpResponse(message, mimetype="application/json", status = status)

def home_data(request):
	tags 		= []
	response 	= {}
	news_articles 	= serializers.serialize("json", News_Article.objects.order_by('dateCreated'))
	news_articles	= eval(news_articles)
	response.setdefault('news_articles', [])

	for article in news_articles:
		temp = {}	
		article	 	= article['fields']
		temp['id'] 	= article['movie']
		temp['title'] 	= article['title']
		picture 	= article['display_picture']
		if not picture:
			picture = "/static/img/Nadigan_logo.jpg"

		temp['image'] 	= picture.split("/")[-1]
		temp['date']  	= article['dateCreated']
		temp['section'] = 'CineNews'
		response['news_articles'].append(temp)

	reviews  = serializers.serialize("json", Reviews.objects.order_by('dateCreated'))
	reviews  = eval(reviews)
	response.setdefault('reviews', [])

	for review in reviews:
		temp = {}
		review 		= review['fields']
		temp['title'] 	= review['review_title']
		temp['id'] 	= review['movie']
		picture 	= review.get('display_picture', '')
		if not picture: 
			picture = "/static/img/Nadigan_logo.jpg"
		temp['image'] 	= picture.split("/")[-1]
		temp['date']  	= review.get('dateCreated') 
		temp['rating'] 	= review.get('rating', '8')
		temp['hits']	= review.get('hits', '')
		temp['section'] = 'Reviews'
		response['reviews'].append(temp)
	
	
	nadigan_spl = serializers.serialize("json", Nadigan_Special.objects.order_by('dateCreated'))
	nadigan_spl = eval(nadigan_spl)
	response.setdefault('nadigan_spl', [])

	for spl in nadigan_spl:
		temp = {}
		temp['id'] 	= spl['pk']
		spl  		= spl['fields']
		temp['title'] 	= article['title']
		tags.append(article['title'])
		picture = article.get('display_picture', '')
		if not picture:
			picture = "/static/img/Nadigan_logo.jpg"
		temp['image'] = picture.split("/")[-1]
		temp['date']  = article['dateCreated']
		temp['section'] = '360Special'
		response['nadigan_spl'].append(temp)

	personality_gallery = serializers.serialize("json", Personality_Gallery.objects.order_by('dateCreated'))
	personality_gallery = eval(personality_gallery)
	response.setdefault('gallery', {})

	for image in personality_gallery:
		temp 		= {}
		image 		= image['fields']
		temp['id'] 	= image['personality']
		temp['title'] 	= image['title']
		picture 	= image.get('image_url', '')
		if not picture:
			picture = "/static/img/Nadigan_logo.jpg"
		temp['image']   = picture.split("/")[-1]
		temp['date']    = image['dateCreated']
		temp['section'] = 'gallery'
		
		response['gallery'].setdefault('personality', []).append(temp)

	movie_gallery = serializers.serialize("json", Movie_Gallery.objects.order_by('dateCreated'))
	movie_gallery = eval(movie_gallery)
	
	for image in movie_gallery:
		temp            = {}
                image           = image['fields']
                temp['id']      = image['movie']
                temp['title']   = image['gallery_title']
                picture         = image.get('image_url', '')
                if not picture:
                        picture = "/static/img/Nadigan_logo.jpg"
                temp['image']   = picture.split("/")[-1]
                temp['date']    = image['dateCreated']
                temp['section'] = 'gallery'

                response['gallery'].setdefault('movie', []).append(temp)

	response['tags'] = tags
	topsection = []
	for section in ['reviews', 'news_articles', 'nadigan_spl']:
		temp = response[section]
		for i in [0, 1, 2]:
			topsection.append(temp[i])
			response[section].remove(temp[i])
	topsection.append(response['gallery']['personality'][1])
	response.setdefault('topsection', topsection)
	
	http_response = _get_http_response(json.dumps(response))
    	#http_response['Access-Control-Allow-Origin'] = "*"

	return http_response

def home(request):
	return render_response(request, 'index.html')

def gallery(request, gallery_id):
	#photos = Personality_Photos.objects.filter(gallery_id=gallery_id)
	#iif photos:
		
	test = {'gallery_id' : gallery_id} #, 'photos' : photos}
	print test
	test = json.dumps(test)
	#print test
	return render_response(request, 'index.html', data=test)


def reviews(request, review_id):
	try:
		reviews = Reviews.objects.filter(id=review_id)
		reviews_response = {}
		if reviews:
			reviews = reviews[0]
			reviews_response['review_title'] = reviews.review_title
			reviews_response['review_text']  = reviews.review_text
			reviews_response['hits']	= reviews.hits
			reviews_response['misses']  = reviews.misses
			reviews_response['interactionCount'] = reviews.interactionCount
			reviews_response['message'] = 'Success'
	except:
		print traceback.format_exc()

	return render(request, 'reviews.html', {'data' : reviews_response})

def nadigan_specials(request, article_id):
	try:
		print "Nadigan Special"
	except:
		print traceback.format_exc()

def get_movie_meta_info(request, movie_id):
	try:
		print "get_movie_meta_info"
	except:
		print traceback.format_exc()
