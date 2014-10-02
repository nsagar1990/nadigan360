# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Organisation.dateCreated'
        db.add_column(u'nd360_organisation', 'dateCreated',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Organisation.dateModified'
        db.add_column(u'nd360_organisation', 'dateModified',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Reviews.dateCreated'
        db.add_column(u'nd360_reviews', 'dateCreated',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Reviews.dateModified'
        db.add_column(u'nd360_reviews', 'dateModified',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Keywords.dateCreated'
        db.add_column(u'nd360_keywords', 'dateCreated',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Keywords.dateModified'
        db.add_column(u'nd360_keywords', 'dateModified',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Nadigan_Special.dateCreated'
        db.add_column(u'nd360_nadigan_special', 'dateCreated',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Nadigan_Special.dateModified'
        db.add_column(u'nd360_nadigan_special', 'dateModified',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Movie_Gallery.dateCreated'
        db.add_column(u'nd360_movie_gallery', 'dateCreated',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Movie_Gallery.dateModified'
        db.add_column(u'nd360_movie_gallery', 'dateModified',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Movie_Videos.dateCreated'
        db.add_column(u'nd360_movie_videos', 'dateCreated',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Movie_Videos.dateModified'
        db.add_column(u'nd360_movie_videos', 'dateModified',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Personality_Gallery.dateCreated'
        db.add_column(u'nd360_personality_gallery', 'dateCreated',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Personality_Gallery.dateModified'
        db.add_column(u'nd360_personality_gallery', 'dateModified',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Personality.dateCreated'
        db.add_column(u'nd360_personality', 'dateCreated',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Personality.dateModified'
        db.add_column(u'nd360_personality', 'dateModified',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'News_Article.dateCreated'
        db.add_column(u'nd360_news_article', 'dateCreated',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'News_Article.dateModified'
        db.add_column(u'nd360_news_article', 'dateModified',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Movie_Photo.dateCreated'
        db.add_column(u'nd360_movie_photo', 'dateCreated',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Movie_Photo.dateModified'
        db.add_column(u'nd360_movie_photo', 'dateModified',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Casts.dateCreated'
        db.add_column(u'nd360_casts', 'dateCreated',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Casts.dateModified'
        db.add_column(u'nd360_casts', 'dateModified',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Personality_Photos.dateCreated'
        db.add_column(u'nd360_personality_photos', 'dateCreated',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Personality_Photos.dateModified'
        db.add_column(u'nd360_personality_photos', 'dateModified',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 1, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Organisation.dateCreated'
        db.delete_column(u'nd360_organisation', 'dateCreated')

        # Deleting field 'Organisation.dateModified'
        db.delete_column(u'nd360_organisation', 'dateModified')

        # Deleting field 'Reviews.dateCreated'
        db.delete_column(u'nd360_reviews', 'dateCreated')

        # Deleting field 'Reviews.dateModified'
        db.delete_column(u'nd360_reviews', 'dateModified')

        # Deleting field 'Keywords.dateCreated'
        db.delete_column(u'nd360_keywords', 'dateCreated')

        # Deleting field 'Keywords.dateModified'
        db.delete_column(u'nd360_keywords', 'dateModified')

        # Deleting field 'Nadigan_Special.dateCreated'
        db.delete_column(u'nd360_nadigan_special', 'dateCreated')

        # Deleting field 'Nadigan_Special.dateModified'
        db.delete_column(u'nd360_nadigan_special', 'dateModified')

        # Deleting field 'Movie_Gallery.dateCreated'
        db.delete_column(u'nd360_movie_gallery', 'dateCreated')

        # Deleting field 'Movie_Gallery.dateModified'
        db.delete_column(u'nd360_movie_gallery', 'dateModified')

        # Deleting field 'Movie_Videos.dateCreated'
        db.delete_column(u'nd360_movie_videos', 'dateCreated')

        # Deleting field 'Movie_Videos.dateModified'
        db.delete_column(u'nd360_movie_videos', 'dateModified')

        # Deleting field 'Personality_Gallery.dateCreated'
        db.delete_column(u'nd360_personality_gallery', 'dateCreated')

        # Deleting field 'Personality_Gallery.dateModified'
        db.delete_column(u'nd360_personality_gallery', 'dateModified')

        # Deleting field 'Personality.dateCreated'
        db.delete_column(u'nd360_personality', 'dateCreated')

        # Deleting field 'Personality.dateModified'
        db.delete_column(u'nd360_personality', 'dateModified')

        # Deleting field 'News_Article.dateCreated'
        db.delete_column(u'nd360_news_article', 'dateCreated')

        # Deleting field 'News_Article.dateModified'
        db.delete_column(u'nd360_news_article', 'dateModified')

        # Deleting field 'Movie_Photo.dateCreated'
        db.delete_column(u'nd360_movie_photo', 'dateCreated')

        # Deleting field 'Movie_Photo.dateModified'
        db.delete_column(u'nd360_movie_photo', 'dateModified')

        # Deleting field 'Casts.dateCreated'
        db.delete_column(u'nd360_casts', 'dateCreated')

        # Deleting field 'Casts.dateModified'
        db.delete_column(u'nd360_casts', 'dateModified')

        # Deleting field 'Personality_Photos.dateCreated'
        db.delete_column(u'nd360_personality_photos', 'dateCreated')

        # Deleting field 'Personality_Photos.dateModified'
        db.delete_column(u'nd360_personality_photos', 'dateModified')


    models = {
        u'nd360.casts': {
            'Meta': {'object_name': 'Casts'},
            'dateCreated': ('django.db.models.fields.DateField', [], {}),
            'dateModified': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.Movie']"}),
            'name': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nd360.Personality']", 'symmetrical': 'False'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'nd360.keywords': {
            'Meta': {'object_name': 'Keywords'},
            'dateCreated': ('django.db.models.fields.DateField', [], {}),
            'dateModified': ('django.db.models.fields.DateField', [], {}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        },
        u'nd360.movie': {
            'Meta': {'object_name': 'Movie'},
            'aggregateRating': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'audience': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'citation': ('django.db.models.fields.TextField', [], {}),
            'dateCreated': ('django.db.models.fields.DateField', [], {}),
            'dateModified': ('django.db.models.fields.DateField', [], {}),
            'datePublished': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'facebook_page': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inLanguage': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'interactionCount': ('django.db.models.fields.IntegerField', [], {}),
            'is_duplicate': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nd360.Keywords']", 'symmetrical': 'False'}),
            'official_website': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'productionCompany': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nd360.Organisation']", 'symmetrical': 'False'}),
            'sub_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'thumbnailUrl': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'trailer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter_handle': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'nd360.movie_gallery': {
            'Meta': {'object_name': 'Movie_Gallery'},
            'dateCreated': ('django.db.models.fields.DateField', [], {}),
            'dateModified': ('django.db.models.fields.DateField', [], {}),
            'gallery_description': ('django.db.models.fields.TextField', [], {}),
            'gallery_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interactionCount': ('django.db.models.fields.IntegerField', [], {}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.Movie']"})
        },
        u'nd360.movie_photo': {
            'Meta': {'object_name': 'Movie_Photo'},
            'dateCreated': ('django.db.models.fields.DateField', [], {}),
            'dateModified': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.Movie_Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'nd360.movie_videos': {
            'Meta': {'object_name': 'Movie_Videos'},
            'dateCreated': ('django.db.models.fields.DateField', [], {}),
            'dateModified': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.Movie']"}),
            'video_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'video_url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'nd360.nadigan_special': {
            'Meta': {'object_name': 'Nadigan_Special'},
            'dateCreated': ('django.db.models.fields.DateField', [], {}),
            'dateModified': ('django.db.models.fields.DateField', [], {}),
            'display_picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nd360.Keywords']", 'symmetrical': 'False'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'video_url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'nd360.news_article': {
            'Meta': {'object_name': 'News_Article'},
            'dateCreated': ('django.db.models.fields.DateField', [], {}),
            'dateModified': ('django.db.models.fields.DateField', [], {}),
            'display_picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interactionCount': ('django.db.models.fields.IntegerField', [], {}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.Movie']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'nd360.organisation': {
            'Meta': {'object_name': 'Organisation'},
            'dateCreated': ('django.db.models.fields.DateField', [], {}),
            'dateModified': ('django.db.models.fields.DateField', [], {}),
            'display_picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'facebook_page': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter_handle': ('django.db.models.fields.TextField', [], {})
        },
        u'nd360.personality': {
            'Meta': {'object_name': 'Personality'},
            'dateCreated': ('django.db.models.fields.DateField', [], {}),
            'dateModified': ('django.db.models.fields.DateField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'facebook_page': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interactionCount': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'other_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter_handle': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'years_active': ('django.db.models.fields.DateField', [], {})
        },
        u'nd360.personality_gallery': {
            'Meta': {'object_name': 'Personality_Gallery'},
            'dateCreated': ('django.db.models.fields.DateField', [], {}),
            'dateModified': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'personality': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.Personality']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'nd360.personality_photos': {
            'Meta': {'object_name': 'Personality_Photos'},
            'dateCreated': ('django.db.models.fields.DateField', [], {}),
            'dateModified': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.Personality_Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'nd360.reviews': {
            'Meta': {'object_name': 'Reviews'},
            'dateCreated': ('django.db.models.fields.DateField', [], {}),
            'dateModified': ('django.db.models.fields.DateField', [], {}),
            'hits': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interactionCount': ('django.db.models.fields.IntegerField', [], {}),
            'misses': ('django.db.models.fields.TextField', [], {}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.Movie']"}),
            'review_text': ('django.db.models.fields.TextField', [], {}),
            'review_title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['nd360']