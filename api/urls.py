from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (FollowViewSet, PostsListViewSet, PostViewSet,
                    UserAdminViewSet, UserViewSet, ViewsViewSet)

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('follow', FollowViewSet, basename='follow')
router.register('users', UserViewSet, basename='users')
router.register('users_admin', UserAdminViewSet, basename='users_admin')
router.register('posts_list', PostsListViewSet, basename='posts_list')
router.register('views', ViewsViewSet, basename='views')


urlpatterns = [
    path('v1/', include(router.urls)),

]
