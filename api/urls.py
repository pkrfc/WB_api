from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FollowViewSet, PostViewSet, UserViewSet


router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('follow', FollowViewSet, basename='follow')
router.register('users', UserViewSet, basename='users')


urlpatterns = [
    path('v1/', include(router.urls)),
]
