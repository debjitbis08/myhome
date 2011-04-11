# Create your views here.

#from django.template import Context, loader
#from django.http import HttpResponse
from django.views.generic import list_detail
from django.shortcuts import get_object_or_404
from myhome.blog.models import Entry

def entry_list(request, num=0):
    return list_detail.object_list(
        request,
        queryset = Entry.objects.all().order_by('-pub_date'),
        paginate_by = 5,
        page = num,
    )

