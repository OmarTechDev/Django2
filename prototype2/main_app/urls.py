from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.booking_register_view import register_booking
from .views.estate_view import EstateViewSet

router = DefaultRouter()

router.register(r'estates',basename='states',viewset=EstateViewSet)
#router.register(r'register_booking',register_booking.as_view(),'register_booking')

urlpatterns =[
    path('register_booking/', register_booking, name='register_booking'),  # Para vistas basadas en funciones
    path('', include(router.urls)),
]