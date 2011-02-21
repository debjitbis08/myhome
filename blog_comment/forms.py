from django import forms
from django.contrib.comments.forms import CommentForm
from django.contrib.comments.models import Comment

class BlogCommentForm(CommentForm):
	
	def __init__(self, *args, **kwargs):
		super(BlogCommentForm, self).__init__(*args, **kwargs)
		self.fields.keyOrder = ['comment', 'name', 'email', 'url']
