import re
from django import template
from myhome.blog.models import Entry

register = template.Library()

@register.filter
def parseusernames(value):
    return re.sub(r'[@]+([A-Za-z0-9-_]+)', r'<a href="http://twitter.com/\1">@\1</a>', value); 
parseusernames.is_safe = True

@register.filter
def parsehashtags(value):
    return re.sub(r'[#]+([A-Za-z0-9-_]+)', r'<a href="http://twitter.com/search/%23\1">#\1</a>', value); 
parsehashtags.is_safe = True
