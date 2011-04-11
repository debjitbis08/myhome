from django.db import models

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
    
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/entry/%s" % (self.slug)

    def get_previous_entry(self):
        return self.get_previous_by_pub_date()

    def get_next_entry(self):
        return self.get_next_by_pub_date()
    
    class Meta:
        verbose_name_plural = "Entries"
