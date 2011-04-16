# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BehanceAuth'
        db.create_table('lifestream_behanceauth', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('base_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('lifestream', ['BehanceAuth'])

        # Adding model 'BehanceAuthor'
        db.create_table('lifestream_behanceauthor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('remote_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('lifestream', ['BehanceAuthor'])

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
            ('behanceauthor', models.ForeignKey(orm['lifestream.behanceauthor'], null=False))
        ))
        db.create_unique('lifestream_behanceitem_authors', ['behanceitem_id', 'behanceauthor_id'])

        # Adding M2M table for field behance_tags on 'BehanceItem'
        db.create_table('lifestream_behanceitem_behance_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('behanceitem', models.ForeignKey(orm['lifestream.behanceitem'], null=False)),
            ('behancetag', models.ForeignKey(orm['lifestream.behancetag'], null=False))
        ))
        db.create_unique('lifestream_behanceitem_behance_tags', ['behanceitem_id', 'behancetag_id'])

        # Adding model 'BehanceTag'
        db.create_table('lifestream_behancetag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('remote_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('lifestream', ['BehanceTag'])


    def backwards(self, orm):
        
        # Deleting model 'BehanceAuth'
        db.delete_table('lifestream_behanceauth')

        # Deleting model 'BehanceAuthor'
        db.delete_table('lifestream_behanceauthor')

        # Deleting model 'BehanceItem'
        db.delete_table('lifestream_behanceitem')

        # Removing M2M table for field authors on 'BehanceItem'
        db.delete_table('lifestream_behanceitem_authors')

        # Removing M2M table for field behance_tags on 'BehanceItem'
        db.delete_table('lifestream_behanceitem_behance_tags')

        # Deleting model 'BehanceTag'
        db.delete_table('lifestream_behancetag')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'remote_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['lifestream']
