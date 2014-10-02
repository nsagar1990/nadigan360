# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movie'
        db.create_table(u'nd360_movie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sub_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('duration', self.gf('django.db.models.fields.IntegerField')()),
            ('trailer', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('aggregateRating', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('audience', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('citation', self.gf('django.db.models.fields.TextField')()),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('inLanguage', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('interactionCount', self.gf('django.db.models.fields.IntegerField')()),
            ('thumbnailUrl', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('facebook_page', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('twitter_handle', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('official_website', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('dateCreated', self.gf('django.db.models.fields.DateField')()),
            ('dateModified', self.gf('django.db.models.fields.DateField')()),
            ('datePublished', self.gf('django.db.models.fields.DateField')()),
            ('is_duplicate', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'nd360', ['Movie'])

        # Adding M2M table for field productionCompany on 'Movie'
        m2m_table_name = db.shorten_name(u'nd360_movie_productionCompany')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'nd360.movie'], null=False)),
            ('organisation', models.ForeignKey(orm[u'nd360.organisation'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'organisation_id'])

        # Adding M2M table for field keywords on 'Movie'
        m2m_table_name = db.shorten_name(u'nd360_movie_keywords')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'nd360.movie'], null=False)),
            ('keywords', models.ForeignKey(orm[u'nd360.keywords'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'keywords_id'])

        # Adding model 'Keywords'
        db.create_table(u'nd360_keywords', (
            ('word', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
        ))
        db.send_create_signal(u'nd360', ['Keywords'])

        # Adding model 'Reviews'
        db.create_table(u'nd360_reviews', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nd360.Movie'])),
            ('review_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('review_text', self.gf('django.db.models.fields.TextField')()),
            ('hits', self.gf('django.db.models.fields.TextField')()),
            ('misses', self.gf('django.db.models.fields.TextField')()),
            ('interactionCount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'nd360', ['Reviews'])

        # Adding model 'Movie_Gallery'
        db.create_table(u'nd360_movie_gallery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nd360.Movie'])),
            ('gallery_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('gallery_description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'nd360', ['Movie_Gallery'])

        # Adding model 'Movie_Photo'
        db.create_table(u'nd360_movie_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nd360.Movie_Gallery'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'nd360', ['Movie_Photo'])

        # Adding model 'Movie_Videos'
        db.create_table(u'nd360_movie_videos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nd360.Movie'])),
            ('video_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('video_description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'nd360', ['Movie_Videos'])

        # Adding model 'News_Article'
        db.create_table(u'nd360_news_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nd360.Movie'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('display_picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'nd360', ['News_Article'])

        # Adding model 'Nadigan_Special'
        db.create_table(u'nd360_nadigan_special', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('display_picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('video_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'nd360', ['Nadigan_Special'])

        # Adding M2M table for field keywords on 'Nadigan_Special'
        m2m_table_name = db.shorten_name(u'nd360_nadigan_special_keywords')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nadigan_special', models.ForeignKey(orm[u'nd360.nadigan_special'], null=False)),
            ('keywords', models.ForeignKey(orm[u'nd360.keywords'], null=False))
        ))
        db.create_unique(m2m_table_name, ['nadigan_special_id', 'keywords_id'])

        # Adding model 'Casts'
        db.create_table(u'nd360_casts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nd360.Movie'])),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'nd360', ['Casts'])

        # Adding M2M table for field name on 'Casts'
        m2m_table_name = db.shorten_name(u'nd360_casts_name')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('casts', models.ForeignKey(orm[u'nd360.casts'], null=False)),
            ('personality', models.ForeignKey(orm[u'nd360.personality'], null=False))
        ))
        db.create_unique(m2m_table_name, ['casts_id', 'personality_id'])

        # Adding model 'Personality'
        db.create_table(u'nd360_personality', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('other_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('years_active', self.gf('django.db.models.fields.DateField')()),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('facebook_page', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('twitter_handle', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('interactionCount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'nd360', ['Personality'])

        # Adding model 'Personality_Gallery'
        db.create_table(u'nd360_personality_gallery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('personality', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nd360.Personality'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image_url', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'nd360', ['Personality_Gallery'])

        # Adding model 'Personality_Photos'
        db.create_table(u'nd360_personality_photos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nd360.Personality_Gallery'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'nd360', ['Personality_Photos'])

        # Adding model 'Organisation'
        db.create_table(u'nd360_organisation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('display_picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('twitter_handle', self.gf('django.db.models.fields.TextField')()),
            ('facebook_page', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'nd360', ['Organisation'])


    def backwards(self, orm):
        # Deleting model 'Movie'
        db.delete_table(u'nd360_movie')

        # Removing M2M table for field productionCompany on 'Movie'
        db.delete_table(db.shorten_name(u'nd360_movie_productionCompany'))

        # Removing M2M table for field keywords on 'Movie'
        db.delete_table(db.shorten_name(u'nd360_movie_keywords'))

        # Deleting model 'Keywords'
        db.delete_table(u'nd360_keywords')

        # Deleting model 'Reviews'
        db.delete_table(u'nd360_reviews')

        # Deleting model 'Movie_Gallery'
        db.delete_table(u'nd360_movie_gallery')

        # Deleting model 'Movie_Photo'
        db.delete_table(u'nd360_movie_photo')

        # Deleting model 'Movie_Videos'
        db.delete_table(u'nd360_movie_videos')

        # Deleting model 'News_Article'
        db.delete_table(u'nd360_news_article')

        # Deleting model 'Nadigan_Special'
        db.delete_table(u'nd360_nadigan_special')

        # Removing M2M table for field keywords on 'Nadigan_Special'
        db.delete_table(db.shorten_name(u'nd360_nadigan_special_keywords'))

        # Deleting model 'Casts'
        db.delete_table(u'nd360_casts')

        # Removing M2M table for field name on 'Casts'
        db.delete_table(db.shorten_name(u'nd360_casts_name'))

        # Deleting model 'Personality'
        db.delete_table(u'nd360_personality')

        # Deleting model 'Personality_Gallery'
        db.delete_table(u'nd360_personality_gallery')

        # Deleting model 'Personality_Photos'
        db.delete_table(u'nd360_personality_photos')

        # Deleting model 'Organisation'
        db.delete_table(u'nd360_organisation')


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
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.Movie']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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