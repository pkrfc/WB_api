from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import (GenericViewSet, ModelViewSet,
                                     ReadOnlyModelViewSet)

from posts.models import Follow, Post, User

from .permissions import IsAuthorOrReadOnly, IsOnlyAdmin
from .serializers import (FollowSerializer, PostListSerializer, PostSerializer,
                          PostViewsSerializer, UserAdminSerializer,
                          UserSerializer)


class UserViewSet(ModelViewSet):
    """User list"""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()


class UserAdminViewSet(UpdateModelMixin, ListModelMixin, GenericViewSet):
    """User list on Admin"""
    serializer_class = UserAdminSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOnlyAdmin]
    queryset = User.objects.all()

    def perform_update(self, serializer):
        serializer.save()


class PostsListViewSet(ReadOnlyModelViewSet):
    """Post list"""
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ('pub_date',)

    def get_queryset(self):
        followed_people = Follow.objects.filter(
            user=self.request.user).values('following'
                                           )
        return Post.objects.filter(author__in=followed_people)


class PostViewSet(ModelViewSet):
    """Post create"""
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ('pub_date',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(ModelViewSet):
    """Follow"""
    serializer_class = FollowSerializer

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()


class ViewsViewSet(UpdateModelMixin, ListModelMixin, GenericViewSet):
    """Read post"""
    serializer_class = PostViewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.all().exclude(views_user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(views_user=self.request.user)
