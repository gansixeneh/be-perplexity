# discover/urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import DiscoverThreadViewSet, ThreadDetailViewSet

router = DefaultRouter()
router.register('discover-thread', DiscoverThreadViewSet, basename='discover-thread')
router.register('thread-detail', ThreadDetailViewSet, basename='thread-detail')

urlpatterns = [
    path('thread-detail/', ThreadDetailViewSet.as_view({'get': 'list'}), name='thread-detail-list'),
]

urlpatterns += router.urls
