# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BehanceAccount'
        db.create_table('lifestream_behanceaccount', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('base_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('remote_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('lifestream', ['BehanceAccount'])

        # Adding model 'BehanceField'
        db.create_table('lifestream_behancefield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('remote_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('lifestream', ['BehanceField'])

        # Adding model 'BehanceImage'
        db.create_table('lifestream_behanceimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('image_height', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('image_width', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('lifestream', ['BehanceImage'])

        # Adding model 'BehanceItem'
        db.create_table('lifestream_behanceitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('remote_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('resource_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('tags', self.gf('tagging.fields.TagField')()),
        ))
        db.send_create_signal('lifestream', ['BehanceItem'])

        # Adding M2M table for field authors on 'BehanceItem'
        db.create_table('lifestream_behanceitem_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('behanceitem', models.ForeignKey(orm['lifestream.behanceitem'], null=False)),
            ('behanceaccount', models.ForeignKey(orm['lifestream.behanceaccount'], null=False))
        ))
        db.create_unique('lifestream_behanceitem_authors', ['behanceitem_id', 'behanceaccount_id'])

        # Adding M2M table for field fields on 'BehanceItem'
        db.create_table('lifestream_behanceitem_fields', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('behanceitem', models.ForeignKey(orm['lifestream.behanceitem'], null=False)),
            ('behancefield', models.ForeignKey(orm['lifestream.behancefield'], null=False))
        ))
        db.create_unique('lifestream_behanceitem_fields', ['behanceitem_id', 'behancefield_id'])


    def backwards(self, orm):
        
        # Deleting model 'BehanceAccount'
        db.delete_table('lifestream_behanceaccount')

        # Deleting model 'BehanceField'
        db.delete_table('lifestream_behancefield')

        # Deleting model 'BehanceImage'
        db.delete_table('lifestream_behanceimage')

        # Deleting model 'BehanceItem'
        db.delete_table('lifestream_behanceitem')

        # Removing M2M table for field authors on 'BehanceItem'
        db.delete_table('lifestream_behanceitem_authors')

        # Removing M2M table for field fields on 'BehanceItem'
        db.delete_table('lifestream_behanceitem_fields')


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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_height': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'image_width': ('django.db.models.fields.PositiveIntegerField', [], {})
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
