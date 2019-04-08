from django.contrib import admin
from .models import Company, Post, Comment, CompanyFavorite

admin.site.register(Company)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(CompanyFavorite)
