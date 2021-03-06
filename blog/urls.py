from django.conf.urls.defaults import *
from myhome.blog.models import Entry
from myhome.blog.views import *
from myhome.blog.feeds import LatestEntriesFeed
from django.views.generic import ListView, DetailView, MonthArchiveView, YearArchiveView

from datetime import date

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
        queryset=Entry.objects.order_by('-pub_date'),
        context_object_name='entry_list',
        paginate_by=5,
    ), name='entry_index'),
    url(r'^archive/(?P<year>\d{4})/$', YearArchiveView.as_view(
        queryset=Entry.objects.order_by('-pub_date'),
        context_object_name='entry_list',
        model=Entry,
        date_field='pub_date',
    ), name='entry_year_index'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', MonthArchiveView.as_view(
        queryset=Entry.objects.order_by('-pub_date'),
        context_object_name='entry_list',
        model=Entry,
        date_field='pub_date',
        paginate_by=5,
    ), name='entry_month_index'),
    url(r'^page/(?P<page>\d+)/$', ListView.as_view(
        queryset=Entry.objects.order_by('-pub_date'),
        context_object_name='entry_list',
        paginate_by=5,
    ), name='entry_index'),
    url(r'^entry/(?P<object_id>\d+)/$', redirect_old_urls),
    url(r'^entry/(?P<slug>[\w\d][-\w\d]*)/$', DetailView.as_view(
        model=Entry,
    ), name="entry"),
    (r'^tags/', include('myhome.tags.urls')),
    (r'^entry/(?P<entry_id>\d+)/subscribe/$', subcribe_by_email),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^latest/feed/$', LatestEntriesFeed()),

    url (r'^search/$',
        view=search,
        name='search'),
)
