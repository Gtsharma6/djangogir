from django.contrib import admin
from .models import Post

# Register your models here.

class Posta(admin.ModelAdmin):

	admin.site.site_header = "Djangogirls Project"
	list_display = ('author','title','created_date')
	list_filter = ('title', )
	search_fields = ['published_date']

admin.site.register(Post, Posta)



