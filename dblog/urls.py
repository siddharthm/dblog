from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dblog.views.home', name='home'),
    # url(r'^dblog/', include('dblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^blog/comment/(?P<blog_id>\d+)/$','blog.views.post_comment'),
	url(r'^blog/entry/(?P<blog_id>\d+)/$','blog.views.entry'),
	url(r'^blog/$','blog.views.index'),
	url(r'^admin/', include(admin.site.urls)),
)
