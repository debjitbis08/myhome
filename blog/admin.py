from myhome.blog.models import Blog
from myhome.blog.models import Entry
from myhome.blog.models import Author
from django.contrib import admin
from taggit.managers import TaggableManager

class EntryAdmin(admin.ModelAdmin):
    fields = ('blog', 'title', 'slug', 'body_text', 'tags', 'author','pub_date')
    prepopulated_fields = {"slug" : ('title',)}

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry, EntryAdmin)
