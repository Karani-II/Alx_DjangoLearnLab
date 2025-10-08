from django.urls import path, include
from .views import PostViewSet, CommentViewSet
from rest_framework.routers  import DefaultRouter 

router = DefaultRouter()
router.register(r'posts' , PostViewSet, basename='Post')
router.register(r'Comments' , CommentViewSet , basename='comment')

urlpatterns = [
    path('',include(router.urls)),

]