# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News_Article.interactionCount'
        db.add_column(u'nd360_news_article', 'interactionCount',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'News_Article.interactionCount'
        db.delete_column(u'nd360_news_article', 'interactionCount')


    models = {
        u'nd360.casts': {
            'Meta': {'object_name': 'Casts'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.Movie']"}),
            'name': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nd360.Personality']", 'symmetrical': 'False'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'nd360.keywords': {
            'Meta': {'object_name': 'Keywords'},
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
            'gallery_description': ('django.db.models.fields.TextField', [], {}),
            'gallery_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.Movie']"})
        },
        u'nd360.movie_photo': {
            'Meta': {'object_name': 'Movie_Photo'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.Movie_Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'nd360.movie_videos': {
            'Meta': {'object_name': 'Movie_Videos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.Movie']"}),
            'video_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'video_url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'nd360.nadigan_special': {
            'Meta': {'object_name': 'Nadigan_Special'},
            'display_picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nd360.Keywords']", 'symmetrical': 'False'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'video_url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'nd360.news_article': {
            'Meta': {'object_name': 'News_Article'},
            'display_picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interactionCount': ('django.db.models.fields.IntegerField', [], {}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.Movie']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'nd360.organisation': {
            'Meta': {'object_name': 'Organisation'},
            'display_picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'facebook_page': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter_handle': ('django.db.models.fields.TextField', [], {})
        },
        u'nd360.personality': {
            'Meta': {'object_name': 'Personality'},
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
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'personality': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.Personality']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'nd360.personality_photos': {
            'Meta': {'object_name': 'Personality_Photos'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.Personality_Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'nd360.reviews': {
            'Meta': {'object_name': 'Reviews'},
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