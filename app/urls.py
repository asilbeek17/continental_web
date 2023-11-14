from django.urls import path
from app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('courses/', courses, name='courses'),
    path('news/', news, name='news'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contact, name='contact'),
]
