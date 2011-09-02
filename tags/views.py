from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from myhome.blog.models import Entry

class EntriesByTagView(ListView):

    context_object_name = "entry_list"

    def get_queryset(self):
        return Entry.objects.filter(tags__slug=self.args[0]).distinct().order_by('-pub_date')
