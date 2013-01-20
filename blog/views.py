# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,Http404
from blog.models import Blog

def index(request):
	latest_blog_list=Blog.objects.all().order_by('-pub_date')[:5]

	return render_to_response('blog/index.html',{'latest_entries':latest_blog_list,})


def entry(request,blog_id):
	try:
		blog=Blog.objects.get(id=blog_id)
	except Blog.DoesNotExist:
		raise Http404
	return render_to_response('blog/entry.html',{'blog':blog,})

