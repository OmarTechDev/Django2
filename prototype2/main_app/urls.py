
from rest_framework.routers import DefaultRouter

from .views.estate_view import EstateViewSet

router = DefaultRouter()

router.register(prefix='estates',basename='states',viewset=EstateViewSet)
#rouer

urlpatterns = router.urls