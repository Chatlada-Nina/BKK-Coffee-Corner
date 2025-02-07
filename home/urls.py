from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name="homepage"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_review/<int:review_id>', views.review_edit,
         name='review_edit'),
    path('<slug:slug>/delete_review/<int:review_id>', views.review_delete,
         name='review_delete'),
]
