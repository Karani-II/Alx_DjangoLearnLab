from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDestroyAPIView,CommentRetrieveUpdateDestroyAPIView,CommentListCreateView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-retrieve-update-destroy'),
    path('comment/',CommentListCreateView.as_view(), name='comment-list-create'),
    path('comment/<int:pk>/',CommentRetrieveUpdateDestroyAPIView.as_views(), name='comment-retrieve-update-destroy'),
]