from django import forms
from django.contrib import admin
from django.db import models
from ckeditor.widgets import CKEditorWidget
from form_utils.admin import ClearableFileFieldsAdmin
from form_utils.widgets import ImageWidget

from da.blog.models import Post

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config_name='default'))
    excerpt = forms.CharField(widget=CKEditorWidget(config_name='basic'))
    class Meta:
        model = Post

class PostAdmin(ClearableFileFieldsAdmin):
    form = PostAdminForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('__unicode__', 'created', 'status')
    list_filter = ('status', 'tags', 'created', 'updated')
    search_fields = ('__unicode__', 'title', 'slug', 'excerpt', 'content')
    formfield_overrides = { models.ImageField: {'widget': ImageWidget}}

admin.site.register(Post, PostAdmin)