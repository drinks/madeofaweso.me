# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'BehanceTag.name'
        db.delete_column('lifestream_behancetag', 'name')

        # Adding field 'BehanceTag.tag'
        db.add_column('lifestream_behancetag', 'tag', self.gf('django.db.models.fields.CharField')(default='', max_length=50), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'BehanceTag.name'
        db.add_column('lifestream_behancetag', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=50), keep_default=False)

        # Deleting field 'BehanceTag.tag'
        db.delete_column('lifestream_behancetag', 'tag')


    models = {
        'lifestream.behanceauth': {
            'Meta': {'object_name': 'BehanceAuth'},
            'base_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'lifestream.behanceauthor': {
            'Meta': {'object_name': 'BehanceAuthor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'remote_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'lifestream.behanceitem': {
            'Meta': {'object_name': 'BehanceItem'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lifestream.BehanceAuthor']", 'symmetrical': 'False'}),
            'behance_tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lifestream.BehanceTag']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'resource_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'lifestream.behancetag': {
            'Meta': {'object_name': 'BehanceTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['lifestream']
