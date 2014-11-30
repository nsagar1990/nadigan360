from django.db import models
from nadigan360.settings import *
from datetime import *

STATIC_DIRS = os.path.join(PROJECT_DIR, 'templates', 'static', 'img')

RATINGS = (
	   (u'0', u'0'),
	   (u'1', u'1'),
	   (u'2', u'2'),
	   (u'3', u'3'),
	   (u'4', u'4'),
	   (u'5', u'5'),
           (u'6', u'6'),
	   (u'7', u'7'),
	   (u'8', u'8'),
	   (u'9', u'9'),
	   (u'10', u'10')
	  )

AUDIENCE = (
	    (u'NA', u'NA'),
	    (u'U', u'U'),
	    (u'U/A', u'U/A'),
	    (u'A', u'A')
	   )

TYPES = (
                (u'A', u'Actor'),
                (u'P', u'Producer'),
                (u'D', u'Director'),
                (u'M', u'Music'),
                (u'E', u'Editor'),
                (u'C', u'Cinematographer')
                )


class Movie(models.Model):
	id		    = models.AutoField(primary_key=True)
	title               = models.CharField(max_length=255)
	sub_title	    = models.CharField(max_length=255)
	duration	    = models.IntegerField()
	productionCompany   = models.ManyToManyField('Organisation')
	trailer		    = models.CharField(max_length=255)
	aggregateRating	    = models.CharField(max_length = 2, choices=RATINGS)
	audience	    = models.CharField(max_length = 2, choices=AUDIENCE)
	citation	    = models.TextField()
	genre		    = models.CharField(max_length=255)
	inLanguage	    = models.CharField(max_length=255)
	interactionCount    = models.IntegerField()
	keywords	    = models.ManyToManyField('Keywords')
	thumbnailUrl	    = models.ImageField(upload_to=STATIC_DIRS)
	description	    = models.TextField()
	url		    = models.CharField(max_length=255)
	facebook_page	    = models.CharField(max_length=255)
	twitter_handle	    = models.CharField(max_length=255)
	official_website    = models.CharField(max_length=255)
	dateCreated         = models.DateField()
        dateModified        = models.DateField()
        datePublished       = models.DateField()
	is_duplicate	    = models.IntegerField(default=0)

	def __str__(self):              # __unicode__ on Python 2
        	return self.title

class Keywords(models.Model):
	word 		    = models.CharField(max_length=255, primary_key=True)
	dateCreated         = models.DateField()
        dateModified        = models.DateField()

	def __str__(self):
		return self.word

class Reviews(models.Model):
	movie 	         	= models.ForeignKey('Movie')
	review_title	 	= models.CharField(max_length=255)
	review_text      	= models.TextField()
	hits	    	 	= models.TextField()
	misses	    		= models.TextField()
	interactionCount    	= models.IntegerField()
	dateCreated         	= models.DateField()
        dateModified        	= models.DateField() 	

	def __str__(self):
		return self.review_title

class Movie_Gallery(models.Model):
	movie               	= models.ForeignKey('Movie')
	gallery_title       	= models.CharField(max_length=255)
	gallery_description 	= models.TextField()
	interactionCount    	= models.IntegerField()
	dateCreated             = models.DateField()
        dateModified            = models.DateField()
	
	def __str__(self):
		return self.gallery_title

class Movie_Photo(models.Model):
	gallery 		= models.ForeignKey('Movie_Gallery')
	image			= models.ImageField(upload_to='templates/static/img/movies')
	description 		= models.TextField()
	dateCreated             = models.DateField()
	dateModified            = models.DateField()


class Movie_Videos(models.Model):
	movie               	= models.ForeignKey('Movie')
	video_url	    	= models.CharField(max_length=255)
	video_description   	= models.CharField(max_length=255)
	dateCreated             = models.DateField()
	dateModified            = models.DateField()


class News_Article(models.Model):
	movie           	= models.ForeignKey('Movie')
	title			= models.CharField(max_length=255)
	text			= models.TextField()
	display_picture		= models.ImageField(upload_to='templates/static/img/movies')
	interactionCount        = models.IntegerField()
	dateCreated             = models.DateField()
        dateModified            = models.DateField()

	def __str__(self):
		return self.title
	 	
class Nadigan_Special(models.Model):
	id 			= models.AutoField(primary_key=True)
	title			= models.CharField(max_length=255)
	text 			= models.TextField() 
	keywords 		= models.ManyToManyField('Keywords')
	display_picture 	= models.ImageField(upload_to='templates/static/img/movies')
	video_url 		= models.CharField(max_length=255)
	dateCreated             = models.DateField()
        dateModified            = models.DateField()

	def __str__(self):
		return self.title

class Casts(models.Model):
	movie_id 		= models.ForeignKey('Movie')
	name	 		= models.ManyToManyField('Personality')
	role	 		= models.CharField(max_length = 2, choices=TYPES)
	dateCreated             = models.DateField()
        dateModified            = models.DateField()

class Personality(models.Model):
	id   		 	= models.AutoField(primary_key=True)
	name 		 	= models.CharField(max_length=255)
	other_name 	 	= models.CharField(max_length=255)
	years_active 	 	= models.DateField()
	date_of_birth 	 	= models.DateField()
	facebook_page    	= models.CharField(max_length=255)
	twitter_handle   	= models.CharField(max_length=255)
	interactionCount 	= models.IntegerField()
	dateCreated             = models.DateField()
        dateModified            = models.DateField()

	def __str__(self):              # __unicode__ on Python 2
        	return self.name

class Personality_Gallery(models.Model):
	personality 		= models.ForeignKey('Personality')
	title 	    		= models.CharField(max_length=255)	
	image_url   		= models.ImageField(upload_to='templates/static/img/movies')
	description 		= models.TextField()
	dateCreated             = models.DateField()
        dateModified            = models.DateField()

class Personality_Photos(models.Model):
	gallery         	= models.ForeignKey('Personality_Gallery')
        image           	= models.ImageField(upload_to='templates/static/img/movies')
        description     	= models.TextField()
	dateCreated             = models.DateField()
        dateModified            = models.DateField()

class Organisation(models.Model):
	id   			= models.AutoField(primary_key=True)
	name 			= models.CharField(max_length=255)
	display_picture 	= models.ImageField(upload_to='templates/static/img/movies') 
	twitter_handle 		= models.TextField()
	facebook_page 		= models.TextField()
	dateCreated             = models.DateField()
        dateModified            = models.DateField()

	def __str__(self):
		return self.name

