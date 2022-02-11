from django.contrib import admin
from .models import News, SportNews, RegistrationData, Publication, Article, TheArticle, Reporter

# Register your models here.

admin.site.register(News)
admin.site.register(SportNews)
admin.site.register(RegistrationData)
admin.site.register(Publication)
admin.site.register(Article)
admin.site.register(TheArticle)
admin.site.register(Reporter)