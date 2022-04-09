from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FollowViewSet, PostViewSet, UserViewSet, PostsListViewSet


router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('follow', FollowViewSet, basename='follow')
router.register('users', UserViewSet, basename='users')
router.register('posts_list', PostsListViewSet, basename='posts_list')


urlpatterns = [
    path('v1/', include(router.urls)),
]
