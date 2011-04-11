from django.contrib.syndication.views import Feed
from myhome.blog.models import Entry 

class LatestEntriesFeed(Feed):
    title = "Debjit Biswas's Weblog"
    link = "/"
    description = "Debjit Biswas's Weblog"

    def items(self):
        return Entry.objects.order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body_text
