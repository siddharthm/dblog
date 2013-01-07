from django.db import models



class User(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=75)
class Blog(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date Published')
	content = models.TextField()
	author_id = models.ForeignKey(User)
class Comment(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date commented')
	content = models.TextField()
	author = models.ForeignKey(User)
	parent = models.ForeignKey(Blog)

