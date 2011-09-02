from django.conf.urls.defaults import *
from myhome.tags.views import EntriesByTagView

urlpatterns = patterns('',
    (r'^([\w\d][-\w\d]*)/$', EntriesByTagView.as_view()),
)
