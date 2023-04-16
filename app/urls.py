from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import ToDOView

router = DefaultRouter()
router.register('', ToDOView)

urlpatterns = [
    path('', include(router.urls)),
]