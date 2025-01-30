from . import views
from django.urls import path

urlpatterns = [
    path('', views.ForumList.as_view(), name='forum'),
    path('new-forum/', views.forum_new, name="new-forum"),
    path('<slug:slug>/', views.forum_detail, name='forum_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]