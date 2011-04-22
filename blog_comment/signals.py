from django.contrib.comments.signals import comment_was_posted
from django.core.mail import mail_admins

def comment_notifier (sender, comment, **kwargs):

    """ Email admins when a new comment is posted """

    if comment.is_public:
        subject = "Comment posted by %s" % (
            comment.user_name)
        body = "%s commented the following on '%s':\n%s" % (
            comment.user_name,
            comment.content_object.title,
            comment.comment)
        mail_admins(subject, body, fail_silently=False, connection=None)
