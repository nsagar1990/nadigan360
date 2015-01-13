from django.conf.urls import patterns, include, url
from nd360.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('nd360.views',
	# Examples:
    	url(r'^$', 'home', name='home'),
    	#url(r'^$', 'nadigan360.views.home', name='home'),
    	#url(r'^nadigan360/', include('nadigan360.foo.urls')),
	url(r'home_data/$', 'home_data', name="home_data"),
	url(r'gallery/(?P<gallery_id>\d+)/$', 'gallery', name="gallery"),
	url(r'reviews/(?P<review_id>\d+)/$', 'reviews', name="reviews"),		

   	# Uncomment the next line to enable the admin:
    	url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
