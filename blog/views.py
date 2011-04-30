# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response
from myhome.blog.models import Entry, CommentSubscriber
from django.http import HttpResponseRedirect
from myhome.blog.forms import CommentSubscriberForm

def redirect_old_urls(request, object_id):
    entry = Entry.objects.get(pk=object_id)
    url = entry.get_absolute_url()
    return HttpResponseRedirect(url)

def subcribe_by_email(request, entry_id):
    if request.method == "POST":
        form = CommentSubscriberForm(request.POST)
        if form.is_valid():
            entry = Entry.objects.get(pk=entry_id)
            subscriber_email = form.cleaned_data['email'] 
            try:
                subscriber = CommentSubscriber.objects.get(email=subscriber_email)
                subscriber.entries.add(entry)
            except:
                subscriber = CommentSubscriber(
                    email = subscriber_email,
                )
                subscriber.save()
                entry.commentsubscriber_set.add(subscriber)
            return HttpResponseRedirect(entry.get_absolute_url())

    else:
        form = CommentSubscriberForm()

    return render_to_response('blog/subscribe.html', {
            'form': form,
        },
        context_instance=RequestContext(request),
    )
