from django.db import models
from django.contrib.comments.moderation import CommentModerator, moderator
from taggit.managers import TaggableManager

import datetime

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body_text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(Author)
    tags = TaggableManager(blank=True)
    
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/entry/%s" % (self.slug)

    def get_previous_entry(self):
        return self.get_previous_by_pub_date()

    def get_next_entry(self):
        return self.get_next_by_pub_date()

    def allow_comments(self):
        delta = datetime.datetime.now() - self.pub_date
        return delta.days < 30
    
    class Meta:
        verbose_name_plural = "Entries"

class CommentSubscriber(models.Model):
    entries = models.ManyToManyField(Entry)
    email = models.EmailField()

    def __unicode__(self):
        return self.email

class EntryModerator(CommentModerator):
    auto_moderate_field = 'pub_date'
    moderate_after = 15

moderator.register (Entry, EntryModerator)
