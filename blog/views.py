# Create your views here.
from django.template import Context,loader
from django.http import HttpResponse
from blog.models import Blog

def index(request):
	latest_blog_list=Blog.objects.all().order_by('-pub_date')[:5]
	t=loader.get_template('blog/index.html')
	c=Context({
		'latest_entries':latest_blog_list,
		})
	output='<br>'.join(["<a href='entry/"+str(p.id)+"'>"+p.title+"</a>" for p in latest_blog_list])
	return HttpResponse(t.render(c))


def entry(request,blog_id):
	return HttpResponse("This is single blog entry with id %d" %int(blog_id))

