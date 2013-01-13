from django.contrib import admin
from blog.models import Blog,User,Comment

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title','author_id','pub_date')
	search_fields=['title']
	date_hierarchy = 'pub_date'
	fieldsets = [
		(None,{'fields':['title','content']}),
		('Blog Info',{'fields':['author_id','pub_date'],'classes':['collapse']}),
		]
admin.site.register(Blog,BlogAdmin)
admin.site.register(User)
admin.site.register(Comment)
