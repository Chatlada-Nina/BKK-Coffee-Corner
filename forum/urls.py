from . import views
from django.urls import path

urlpatterns = [
    path('', views.ForumList.as_view(), name='forum'),
    path('<slug:slug>/', views.forum_detail, name='forum_detail'),
]