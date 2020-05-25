from django.shortcuts import render
from rest_framework import viewsets, status
from posts.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly



class PostViewSet(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentsViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_post_with_specific_key(self):
        post = get_object_or_404(Post, id=self.kwargs['posts_pk'])
        return post

    def get_queryset(self):
        queryset = Comment.objects.filter(post=self.get_post_with_specific_key()).all()
        return queryset







