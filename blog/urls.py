from django.conf.urls.defaults import *
from myhome.blog.models import Entry
from myhome.blog.feeds import LatestEntriesFeed

info_dict = {
	'queryset': Entry.objects.order_by('-pub_date'),
	'template_object_name': 'entry',
}
info_dict_design = {
	'queryset': Entry.objects.order_by('-pub_date'),
	'template_object_name': 'entry',
	'design': 'True',
}

urlpatterns = patterns('',
    url(r'^$','myhome.blog.views.entry_list',name='entry_index'),
    url(r'^page/(?P<num>\d+)/$','myhome.blog.views.entry_list',name='entry_index_paginated'),
    url(r'^entry/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict, name="entry"),
    (r'^comments/', include('django.contrib.comments.urls')),
	(r'^latest/feed/$', LatestEntriesFeed()),
    url(r'^design/$','myhome.blog.views.entry_list',{'design':'True'},name='design_entry_index'),
    url(r'^design/$page/(?P<num>\d+)/$','myhome.blog.views.entry_list',{'design':'True'},name='design_entry_index_paginated'),
    url(r'^design/$entry/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict_design, name="design_entry"),
    (r'^design/$comments/', include('django.contrib.comments.urls')),
	(r'^latest/feed/$', LatestEntriesFeed()),
)
