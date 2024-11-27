from abc import ABC, abstractmethod
from typing import Any
from django.http import JsonResponse
from rest_framework.views import APIView

class BaseAPIView(ABC, APIView):
    """Clase base abstracta para vistas"""

    @abstractmethod
    def get_data(self, *args, **kwargs) -> Any:
        pass

    #Incluir esta seccion donde se maneja la clase abstracta y concreta para manejo de respuesta??
    def get(self, request, *args, **kwargs):
        try:
            data = self.get_data(*args, **kwargs)
            return JsonResponse({'success': True, 'data': data}, status=200)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    @abstractmethod
    def post_data(self, *args, **kwargs) -> Any:
        pass

    #Incluir esta seccion donde se maneja la clase abstracta y concreta para manejo de respuesta??
    def post(self, request, *args, **kwargs):
        try:
            data = self.post_data(*args, **kwargs)
            return JsonResponse({'success': True, 'data': data}, status=201)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
