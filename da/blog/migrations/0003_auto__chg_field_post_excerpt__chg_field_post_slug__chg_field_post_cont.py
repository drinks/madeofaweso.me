# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Post.excerpt'
        db.alter_column('blog_post', 'excerpt', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Post.slug'
        db.alter_column('blog_post', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100))

        # Adding index on 'Post', fields ['slug']
        db.create_index('blog_post', ['slug'])

        # Changing field 'Post.content'
        db.alter_column('blog_post', 'content', self.gf('django.db.models.fields.TextField')())


    def backwards(self, orm):
        
        # Removing index on 'Post', fields ['slug']
        db.delete_index('blog_post', ['slug'])

        # Changing field 'Post.excerpt'
        db.alter_column('blog_post', 'excerpt', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'Post.slug'
        db.alter_column('blog_post', 'slug', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True))

        # Changing field 'Post.content'
        db.alter_column('blog_post', 'content', self.gf('ckeditor.fields.RichTextField')())


    models = {
        'blog.post': {
            'Meta': {'object_name': 'Post'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excerpt': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'draft'", 'max_length': '30'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['blog']
