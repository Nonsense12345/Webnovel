from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Author)
admin.site.register(NovelGenre)
admin.site.register(NovelAuthor)
admin.site.register(Novel)
admin.site.register(Chapter)
admin.site.register(Comment)
admin.site.register(Genre)
admin.site.register(Rating)