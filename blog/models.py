from django.db import models
import datetime
from django.utils import timezone


class User(models.Model):
	def __unicode__(self):
		return self.name
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=75)
class Blog(models.Model):
	def __unicode__(self):
		return self.title
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date Published')
	content = models.TextField()
	author_id = models.ForeignKey(User)
class Comment(models.Model):
	def __unicode__(self):
		return self.title
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date commented')
	content = models.TextField()
	author = models.ForeignKey(User)
	parent = models.ForeignKey(Blog)
	def is_old(self):
		return self.pub_date <= timezone.now() - datetime.timedelta(days=30) 

