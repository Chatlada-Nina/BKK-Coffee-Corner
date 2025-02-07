from django.urls import path
from . import views


urlpatterns = [
    path('', views.ForumList.as_view(), name='forum'),
    path('new-forum/', views.forum_new, name="new-forum"),
    path('<slug:slug>/', views.forum_detail, name='forum-detail'),
    path('forum_edit/<int:forum_id>/', views.forum_edit, name='forum-edit'),
    path('delete_forum/<int:forum_id>/', views.forum_delete,
         name='forum-delete'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit,
         name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete,
         name='comment_delete'),
]
