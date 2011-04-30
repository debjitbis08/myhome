from django import forms

class CommentSubscriberForm(forms.Form):
    email = forms.EmailField()
