from django import forms
from django.contrib import admin
from django.db import models

from moa.lifestream import models

class SocialNetworkAdmin(admin.ModelAdmin):
    pass

class BehanceAccountAdmin(admin.ModelAdmin):
    list_display = ('name','active',)

class BehanceFieldAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("field",),}

class BehanceImageAdmin(admin.ModelAdmin):
    pass

class BehanceItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",),}
    list_display = ('__unicode__', 'created',)
    list_filter = ('created',)

    save_on_top = True

admin.site.register(models.SocialNetwork, SocialNetworkAdmin)
admin.site.register(models.BehanceAccount, BehanceAccountAdmin)
admin.site.register(models.BehanceField, BehanceFieldAdmin)
admin.site.register(models.BehanceImage, BehanceImageAdmin)
admin.site.register(models.BehanceItem, BehanceItemAdmin)