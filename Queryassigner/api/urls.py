from rest_framework.routers import DefaultRouter
from .views import QueryViewsets,ResponseViewsets

router = DefaultRouter()
router.register('queries', QueryViewsets)
router.register('responses', ResponseViewsets)

from django.urls import path,include

urlpatterns = [
    path('', include(router.urls)),
]

