from django.contrib.comments.signals import comment_was_posted
from django.core.mail import mail_admins

@receiver(comment_was_posted)
def comment_notifier (sender, comment, request):

    """ Email admins when a new comment is posted """

    if comment.is_public:
        subject = "Comment posted by %s" % (
            comment.user_name)
        body = "%s posted commented the following on the entry %s: %s" % (
            comment.user_name,
            comment.content_object.title,
            comment.comment)
        mail_admins(subject, body, fail_silently=False, connection=None)
