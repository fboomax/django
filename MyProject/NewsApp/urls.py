from django.urls import path
from .views import *
urlpatterns = [
    path('', Home, name = 'Home'),
    path('about/', About, name = 'About'),
    path('news/', NewsViews, name = 'Latest News'),
    path('newsdate/',NewsDate, name = 'News Date'),
    path('newsdate/<int:year>',NewsDate, name = 'News Date'),
    path('contact/', Contact, name = 'Contact'),
    path('signup/', Register, name =  'Registers'),
    path('addUser/', addUser, name = 'addUser'),
    path('modalform/', modalform, name = 'form'),
    path('addmodalform/', addmodalform, name ='modalform'), 
    path('newaricle/',ThisNewArticle, name='News & Articles')
]
