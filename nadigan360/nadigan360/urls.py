from django.conf.urls import patterns, include, url
from nd360.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('nd360.views',
    	url(r'^$', 'home', name='home'),
	url(r'home_data/$', 'home_data', name="home_data"),

	#reviews
	url(r'^reviews/(?P<review_id>\d+)/$', 'reviews', name="reviews"),		
	url(r'^reviews', 'all_reviews', name='all_reviews'),

	#Cinenews
	url(r'^cinenews/(?P<article_id>\d+)/$', 'cinenews', name='cinenews'),
	url(r'^cinenews', 'all_cinenews', name="all_cinenews"),

	#360specials
	url(r'^360specials', 'nadigan360', name="nadigan360"),
	url(r'^360specials/(?P<article_id>\d+)/$', 'nadigan_spl', name='nadigan_spl'),

	#gallery
	url(r'gallery', 'galleries', name="galleries"),
	url(r'gallery/(?P<gallery_id>\d+)/$', 'gallery', name="gallery"),

   	# Uncomment the next line to enable the admin:
    	url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
