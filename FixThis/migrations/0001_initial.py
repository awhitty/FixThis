# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Request'
        db.create_table('FixThis_request', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 11, 8, 0, 0))),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('urgency', self.gf('django.db.models.fields.IntegerField')()),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=36, decimal_places=16)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=36, decimal_places=16)),
        ))
        db.send_create_signal('FixThis', ['Request'])


    def backwards(self, orm):
        # Deleting model 'Request'
        db.delete_table('FixThis_request')


    models = {
        'FixThis.request': {
            'Meta': {'object_name': 'Request'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '36', 'decimal_places': '16'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '36', 'decimal_places': '16'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 11, 8, 0, 0)'}),
            'urgency': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['FixThis']