from django.db import models

# Create your models here.

class Movie(models.Model):
	id			= models.AutoField(primary_key=True)
	movie_name		= models.CharField(max_length=30)
	sub_title		= models.CharField(max_length=100)
	casting			= models.TextField() 
	director		= models.CharField(max_length=20)
	producer		= models.CharField(max_length=20)
	image_link		= models.CharField(max_length=255)
	genre			= models.CharField(max_length=50)
	plot 			= models.TextField()
	rating			= models.IntegerField()
	base_popularity		= models.IntegerField()
	release_date		= models.DateField()
	total_duration		= models.CharField(max_length=10)
	other_websites_rating	= models.CharField(max_length=10)
	wikipedia_link		= models.CharField(max_length=255)
	budget 			= models.CharField(max_length=50)
	created_at		= models.DateField()
	modifed_at		= models.DateField()

class Movie_Casts(models.Model):
	movie_id        	= models.ForeignKey(Movie)
	actors			= models.CharField(max_length=255)
	actress			= models.CharField(max_length=255)
        supporting_casts	= models.CharField(max_length=255)
	comdians		= models.CharField(max_length=255)

class Movie_Gallery(models.Model):
	movie_id                = models.ForeignKey(Movie)
	text			= models.TextField()
	image_link		= models.TextField()	

class Movie_Rating(models.Model):
	movie_id                = models.ForeignKey(Movie)
	overall_rating		= models.CharField(max_length=10)
	music_rating		= models.CharField(max_length=10)
	performance_rating	= models.CharField(max_length=10)
	special_effects_rating	= models.CharField(max_length=10)
	directors_rating	= models.CharField(max_length=10)

class Movie_Technicians(models.Model):
        movie_id        	= models.ForeignKey(Movie)
        cinematogapy    	= models.CharField(max_length=50)
        stunt           	= models.CharField(max_length=50)
        choregrahpy     	= models.CharField(max_length=50)
        art_director    	= models.CharField(max_length=50)

class Movie_Reviews(models.Model):
        movie_id        	= models.ForeignKey(Movie)
        review_text     	= models.TextField()

class Movie_User_Comments(models.Model):
	movie_id        	= models.ForeignKey(Movie)
	user_name		= models.CharField(max_length=50)
	email_id		= models.CharField(max_length=50)
	text			= models.TextField()
	likes			= models.IntegerField()
	dislikes		= models.IntegerField()

#class Movie_Sentiment(models.Model):

#class Movie_Sentiment_Info(models.Model):

#class Movie_Sentiment_Text(models.Model):

