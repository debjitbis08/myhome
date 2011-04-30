from django.contrib.comments.signals import comment_was_posted
from django.core.mail import send_mass_mail
from myhome.blog.models import CommentSubscriber
from django.conf import settings

def comment_notifier (sender, comment, **kwargs):

    """ Email admins when a new comment is posted """
    if comment.is_public:
        subscribers = [subscriber.email for subscriber in CommentSubscriber.objects.filter(entries=comment.content_object.id)]
        subject = "New comment for %s" % (
            comment.content_object.title)
        body = "%s had the following to say:\n%s" % (
            comment.user_name,
            comment.comment)
        if comment.user_name in subscribers:
            indx = subscribers.index(comment.user_name)
            del subscribers[indx]

        subscribers = subscribers + [admins[1] for admins in settings.ADMINS]

        messages = ()
        for subscriber in subscribers:
            messages = messages + ((subject, body, "admin@debjitbiswas.com", [subscriber]),)
        
        send_mass_mail(messages, fail_silently=False)
