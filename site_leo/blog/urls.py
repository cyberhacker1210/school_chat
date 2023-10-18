from django.urls import path
from .views import index, Planning, planning_g1
urlpatterns = [
    path('', index, name="blog-index"),
    path('planning/', Planning, name="planning"),
    path('G1/', planning_g1, name="planningG1"),
]