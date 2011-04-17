from django import forms
from django.contrib import admin
from django.db import models
from ckeditor.widgets import CKEditorWidget
from sorl.thumbnail.admin import AdminImageMixin

from moa.blog.models import Post

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config_name='default'))
    excerpt = forms.CharField(widget=CKEditorWidget(config_name='default'))
    class Meta:
        model = Post

class PostAdmin(AdminImageMixin, admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {"slug": ("title",),}
    list_display = ('__unicode__', 'created', 'tags', 'status',)
    list_filter = ('status', 'created', 'updated',)
    list_editable = ('tags', 'status',)
    search_fields = ('title', 'slug', 'excerpt', 'content', 'tags',)
    date_hierarchy = 'created'
    
    list_select_related = True
    save_on_top = True

admin.site.register(Post, PostAdmin)