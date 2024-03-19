from django.contrib import admin
from djangoapp.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)