from django.contrib.comments.models import Comment
from django.contrib.comments.signals import comment_was_posted
from myhome.blog_comment.signals import comment_notifier

comment_was_posted.connect(comment_notifier, sender=Comment)
