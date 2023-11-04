from django.contrib import admin
from django.urls import path, include
from .views import index
from chat import views


urlpatterns = [
    path('', index, name="index"),
    path('blog/', include("blog.urls")),
    path('admin/', admin.site.urls),
    path('chat/', include("chat.urls")),
    path('<str:room>/', views.room, name="room"),
    path('getMessages/<str:room>/', views.getMessages, name="getMessages"),
    path('send', views.send, name="send"),
]
