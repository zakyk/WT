# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'PointsOfInterest_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('friends', self.gf('django.db.models.fields.related.ForeignKey')(default='null', to=orm['PointsOfInterest.User'], on_delete=models.SET_DEFAULT, blank=True)),
        ))
        db.send_create_signal(u'PointsOfInterest', ['User'])

        # Adding model 'CategoryOfPoi'
        db.create_table(u'PointsOfInterest_categoryofpoi', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'PointsOfInterest', ['CategoryOfPoi'])

        # Adding model 'Photo'
        db.create_table(u'PointsOfInterest_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'PointsOfInterest', ['Photo'])

        # Adding model 'PointOfInterest'
        db.create_table(u'PointsOfInterest_pointofinterest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PointsOfInterest.User'])),
            ('latitude', self.gf('django.db.models.fields.FloatField')(max_length=30)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(max_length=30)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PointsOfInterest.CategoryOfPoi'])),
            ('photos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PointsOfInterest.Photo'])),
        ))
        db.send_create_signal(u'PointsOfInterest', ['PointOfInterest'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'PointsOfInterest_user')

        # Deleting model 'CategoryOfPoi'
        db.delete_table(u'PointsOfInterest_categoryofpoi')

        # Deleting model 'Photo'
        db.delete_table(u'PointsOfInterest_photo')

        # Deleting model 'PointOfInterest'
        db.delete_table(u'PointsOfInterest_pointofinterest')


    models = {
        u'PointsOfInterest.categoryofpoi': {
            'Meta': {'object_name': 'CategoryOfPoi'},
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'PointsOfInterest.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'PointsOfInterest.pointofinterest': {
            'Meta': {'object_name': 'PointOfInterest'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PointsOfInterest.CategoryOfPoi']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'max_length': '30'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'max_length': '30'}),
            'photos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PointsOfInterest.Photo']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PointsOfInterest.User']"})
        },
        u'PointsOfInterest.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'friends': ('django.db.models.fields.related.ForeignKey', [], {'default': "'null'", 'to': u"orm['PointsOfInterest.User']", 'on_delete': 'models.SET_DEFAULT', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['PointsOfInterest']