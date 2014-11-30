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


def get_reviews(request):
	page = request.GET.get('page', 'homepage')
	review_id = request.GET.get('review_id', '')

	if page == "homepage":
		reviews = Reviews.objects.all().order_by('-dateCreated')[2:12]
	elif page == "details":
		reviews = Reviews.objects.filter(id=review_id)
	else:
		print "Need to add condition here"	

	
	response = []
	for review in reviews:
		temp = dict(id = review.id, review_title = review.review_title, review_text = "this is test text !!" * 30, section="Reviews")
		response.append(temp)
	
	http_response = _get_http_response(json.dumps(response))
        http_response['Access-Control-Allow-Origin'] = "*"

        return http_response


def get_news(request):
	page = request.GET.get('page', 'homepage')
        article_id = request.GET.get('article_id', '')

        if page == "homepage":
                news_article = News_article.objects.all().order_by('-dateCreated')[2:12]
        elif page == "details":
                news_article = News_article.objects.filter(id=article_id)
        else:
                print "Need to add condition here"

        response = []
        for news in reviews:
		temp = dict(id = news.id, title = news.title, display_picture = news.display_picture, interactionCount = news.interactionCount, section = "CineNews")
                response.append(temp)

        http_response = _get_http_response(json.dumps(response))
        http_response['Access-Control-Allow-Origin'] = "*"

        return http_response


def gallery(request):
	page = request.GET.get('page', 'homepage')
        gallery_id = request.GET.get('gallery_id', '')
        
        if page == "homepage":
                news_article = Movie_Gallery.objects.all().order_by('-dateCreated')[2:12]
        elif page == "details":
                news_article = Movie_Gallery.objects.filter(id=gallery_id)
        else:
                print "Need to add condition here"
        
        response = []
        for news in reviews:
		news = dict(id = news.id, title = news.title, movie_id = news.movie_id)
                response.append(temp)

        http_response = _get_http_response(json.dumps(response))
        http_response['Access-Control-Allow-Origin'] = "*"

        return http_response


def home(request):
	print "Came here"
