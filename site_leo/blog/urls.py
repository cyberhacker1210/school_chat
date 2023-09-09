from django.urls import path
from .views import index, Planning
urlpatterns = [
    path('', index, name="blog-index"),
    path('planning/', Planning, name="planning"),
]