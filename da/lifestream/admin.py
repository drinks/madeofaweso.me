from django import forms
from django.contrib import admin
from django.db import models

from da.lifestream import models

class BehanceAuthAdmin(admin.ModelAdmin):
    pass
    
class BehanceAuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",),}

class BehanceItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",),}
    list_display = ('__unicode__', 'created',)
    list_filter = ('created',)

    save_on_top = True

class BehanceTagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("tag",),}

admin.site.register(models.BehanceAuth, BehanceAuthAdmin)
admin.site.register(models.BehanceAuthor, BehanceAuthorAdmin)
admin.site.register(models.BehanceItem, BehanceItemAdmin)
admin.site.register(models.BehanceTag, BehanceTagAdmin)