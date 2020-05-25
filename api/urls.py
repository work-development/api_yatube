from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import PostViewSet, CommentsViewSet
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework_nested import routers

router = DefaultRouter()
router.register('api/v1/posts', PostViewSet)
commets_router = routers.NestedSimpleRouter(router, r'api/v1/posts', lookup='posts')
commets_router.register(r'comments', CommentsViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(commets_router.urls)),
]

urlpatterns += [
    path('api/v1/api-token-auth/', views.obtain_auth_token)
]