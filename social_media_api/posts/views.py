from rest_framework import generics, permissions,filters ,viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from .models import Post, Comment , Like 
from .serializers import PostSerializer, CommentSerializer
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from .models import Post, Like
from notifications.models import Notification


class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']  


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    def perform_update(self, serializer):
        if self.request.user != self.get_object().author:
            raise permissions.PermissionDenied("You cannot edit another user’s post.")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise permissions.PermissionDenied("You cannot delete another user’s post.")
        instance.delete()



class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    def perform_update(self, serializer):
        if self.request.user != self.get_object().author:
            raise PermissionDenied("You can only edit your own comment.")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise PermissionDenied("You can only delete your own comment.")
        instance.delete()

class FeedView(generics.ListAPIView):

    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')



@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    existing_like = Like.objects.filter(user=request.user, post=post).first()
    if existing_like:
        return Response({'error': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    
    Like.objects.create(user=request.user, post=post)

    
    if post.author != request.user:  
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.id
        )

    return Response({'message': 'Post liked successfully.'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like = Like.objects.filter(user=request.user, post=post).first()

    if not like:
        return Response({'error': 'You have not liked this post yet.'}, status=status.HTTP_400_BAD_REQUEST)

    like.delete()
    return Response({'message': 'Post unliked successfully.'}, status=status.HTTP_200_OK)






        







# Create your views here.
