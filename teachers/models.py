from django.db import models

from django import forms


# Create your models here.

class Message(models.Model):
	teacher = models.CharField(max_length = 30)
	content = models.TextField()

class MessageForm(forms.Form):
	teacher = forms.CharField(max_length = 30)
	content = forms.CharField(widget = forms.Textarea)

