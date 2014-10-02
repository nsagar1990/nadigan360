from django.contrib import admin
from nd360.models import *


class Movie_Photos(admin.TabularInline):
	model = Movie_Photo
	extra = 0

class Movie_Gallery_Admin(admin.ModelAdmin):
	inlines = [Movie_Photos]

class Personality_Photo(admin.TabularInline):
	model = Personality_Photos
	extra = 0

class Personality_Gallery_Admin(admin.ModelAdmin):
	inlines = [Personality_Photo]
	
admin.site.register(Movie)
admin.site.register(Personality)
admin.site.register(Organisation)
admin.site.register(Casts)
admin.site.register(Keywords)
admin.site.register(Movie_Gallery, Movie_Gallery_Admin)
admin.site.register(Movie_Videos)
admin.site.register(News_Article)
admin.site.register(Nadigan_Special)
admin.site.register(Personality_Gallery, Personality_Gallery_Admin)
admin.site.register(Reviews)
