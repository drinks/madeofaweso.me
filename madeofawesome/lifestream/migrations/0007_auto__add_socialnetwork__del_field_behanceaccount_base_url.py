# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SocialNetwork'
        db.create_table('lifestream_socialnetwork', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('api_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('lifestream', ['SocialNetwork'])

        # Deleting field 'BehanceAccount.base_url'
        db.delete_column('lifestream_behanceaccount', 'base_url')


    def backwards(self, orm):
        
        # Deleting model 'SocialNetwork'
        db.delete_table('lifestream_socialnetwork')

        # Adding field 'BehanceAccount.base_url'
        db.add_column('lifestream_behanceaccount', 'base_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True), keep_default=False)


    models = {
        'lifestream.behanceaccount': {
            'Meta': {'object_name': 'BehanceAccount'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'lifestream.behancefield': {
            'Meta': {'object_name': 'BehanceField'},
            'field': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'lifestream.behanceimage': {
            'Meta': {'object_name': 'BehanceImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lifestream.BehanceItem']"})
        },
        'lifestream.behanceitem': {
            'Meta': {'object_name': 'BehanceItem'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lifestream.BehanceAccount']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lifestream.BehanceField']", 'null': 'True', 'blank': 'True'}),
            'frozen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'resource_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'lifestream.socialnetwork': {
            'Meta': {'object_name': 'SocialNetwork'},
            'api_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['lifestream']
