from django.contrib import admin
from .models import *

class PostingAdmin(admin.ModelAdmin):
  list_display = ["title", "company", "_get_tags"]

class PostingTagAdmin(admin.ModelAdmin):
  list_display = ["posting", "tag"]


# Register your models here.
admin.site.register(Posting, PostingAdmin)
admin.site.register(Tag)
admin.site.register(PostingTag, PostingTagAdmin)
admin.site.register(Profile)
