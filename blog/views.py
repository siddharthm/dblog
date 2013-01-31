# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse,Http404
from blog.models import Blog,Comment,User
from django.template import RequestContext
import datetime
from django.utils import timezone
def index(request):
	latest_blog_list=Blog.objects.all().order_by('-pub_date')[:5]

	return render_to_response('blog/index.html',{'latest_entries':latest_blog_list,})


def entry(request,blog_id):
	try:
		blog=Blog.objects.get(id=blog_id)
		comments=Comment.objects.filter(parent=blog)
	except Blog.DoesNotExist:
		raise Http404
	return render_to_response('blog/entry.html',{'blog':blog,'comments':comments},context_instance=RequestContext(request))

def post_comment(request,blog_id):
	blog=get_object_or_404(Blog,id=blog_id)
	titl=request.POST['title']
	content=request.POST['content']
	c=Comment(title=titl,pub_date=timezone.now(),parent=blog,content=content,author=User.objects.get(id=1))
	c.save()
	return HttpResponse('Your comment has been posted!')
