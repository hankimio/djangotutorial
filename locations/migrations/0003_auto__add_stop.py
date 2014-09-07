# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stop'
        db.create_table(u'locations_stop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stop_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=6)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=6)),
        ))
        db.send_create_signal(u'locations', ['Stop'])


    def backwards(self, orm):
        # Deleting model 'Stop'
        db.delete_table(u'locations_stop')


    models = {
        u'locations.stop': {
            'Meta': {'object_name': 'Stop'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'stop_id': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'locations.vehicle': {
            'Meta': {'object_name': 'Vehicle'},
            'heading': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'predictable': ('django.db.models.fields.BooleanField', [], {}),
            'route_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'run_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'seconds_since_report': ('django.db.models.fields.IntegerField', [], {}),
            'vehicle_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['locations']