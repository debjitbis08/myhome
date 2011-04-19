# Create your views here.

#from django.template import Context, loader
#from django.http import HttpResponse
from django.views.generic import list_detail
from django.shortcuts import get_object_or_404
from myhome.blog.models import Entry
from django.http import HttpResponseRedirect

def redirect_old_urls(request, object_id):
    entry = Entry.objects.get(pk=object_id)
    url = entry.get_absolute_url()
    return HttpResponseRedirect(url)

