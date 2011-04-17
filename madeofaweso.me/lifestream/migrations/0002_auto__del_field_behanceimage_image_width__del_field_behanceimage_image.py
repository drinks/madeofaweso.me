# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'BehanceImage.image_width'
        db.delete_column('lifestream_behanceimage', 'image_width')

        # Deleting field 'BehanceImage.image_height'
        db.delete_column('lifestream_behanceimage', 'image_height')

        # Adding field 'BehanceImage.item'
        db.add_column('lifestream_behanceimage', 'item', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['lifestream.BehanceItem']), keep_default=False)

        # Changing field 'BehanceImage.image'
        db.alter_column('lifestream_behanceimage', 'image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100))


    def backwards(self, orm):
        
        # Adding field 'BehanceImage.image_width'
        db.add_column('lifestream_behanceimage', 'image_width', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)

        # Adding field 'BehanceImage.image_height'
        db.add_column('lifestream_behanceimage', 'image_height', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)

        # Deleting field 'BehanceImage.item'
        db.delete_column('lifestream_behanceimage', 'item_id')

        # Changing field 'BehanceImage.image'
        db.alter_column('lifestream_behanceimage', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))


    models = {
        'lifestream.behanceaccount': {
            'Meta': {'object_name': 'BehanceAccount'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'base_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'remote_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'lifestream.behancefield': {
            'Meta': {'object_name': 'BehanceField'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'resource_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['lifestream']
