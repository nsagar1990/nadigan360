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

import json
from django.core import serializers

def render_response(request, template, data=None):
	data = data or {}  
    	r = RequestContext(request)
    	data['ref_path'] = request.get_full_path()
    	return render_to_response(template, data, context_instance=r)

def _get_http_response(message, status=200):
    	return HttpResponse(message, mimetype="application/json", status = status)

def home(request):
	response 	= {}
	news_articles 	= serializers.serialize("json", News_Article.objects.order_by('dateCreated'))
	news_articles	= eval(news_articles)
	response.setdefault('news_articles', [])

	for article in news_articles:
		temp = {}	
		article	 = article['fields']
		temp['id'] = article['movie']
		temp['title'] 	= article['title']
		picture = article['display_picture'].replace("templates/static/img/movies", "http://nd360.niranjanfellow.biz/static/images")
		if not picture:
			picture = "http://nd360.niranjanfellow.biz/static/images/no-image.jpg"
		temp['image'] = picture
		temp['date']  = article['dateCreated']
		temp['section'] = 'Cine News'
		response['news_articles'].append(temp)

	reviews  = serializers.serialize("json", Reviews.objects.order_by('dateCreated'))
	reviews  = eval(reviews)
	response.setdefault('reviews', [])

	for review in reviews:
		temp = {}
		review = review['fields']
		temp['title'] = review['review_title']
		temp['id'] = review['movie']
		picture = review.get('display_picture', '').replace("templates/static/img/movies", "http://nd360.niranjanfellow.biz/static/images")
		if not picture: 
			picture = "http://nd360.niranjanfellow.biz/static/images/no-image.jpg"
		temp['image'] 	= picture
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
		temp['id'] = spl['pk']
		spl  = spl['fields']
		temp['title'] = article['title']
		picture = article.get('display_picture', '').replace("templates/static/img/movies", "http://nd360.niranjanfellow.biz/static/images")
		if not picture:
			picture = "http://nd360.niranjanfellow.biz/static/images/no-image.jpg"
		temp['image'] = picture
		temp['date']  = article['dateCreated']
		temp['section'] = '360 Special'
		response['nadigan_spl'].append(temp)

	personality_gallery = serializers.serialize("json", Personality_Gallery.objects.order_by('dateCreated'))
	personality_gallery = eval(personality_gallery)
	response.setdefault('gallery', [])

	for image in personality_gallery:
		temp = {}
		image = image['fields']
		temp['id'] = image['personality']
		temp['title'] = image['title']
		picture = image.get('image_url', '').replace("templates/static/img/movies", "http://nd360.niranjanfellow.biz/static/images")
		if not picture:
			picture = "http://nd360.niranjanfellow.biz/static/images/no-image.jpg"
		temp['image']   = picture
		temp['date']    = image['dateCreated']
		temp['section'] = 'gallery'
		response['gallery'].append(temp)


	topsection = []
	for section in ['reviews', 'news_articles']:
		temp = response[section]
		for i in [0, 1, 2]:
			topsection.append(temp[i])
			response[section].remove(temp[i])
	topsection.append(response['gallery'][1])
	response.setdefault('topsection', topsection)
	
	http_response = _get_http_response(json.dumps(response))
    	http_response['Access-Control-Allow-Origin'] = "*"

	return http_response
