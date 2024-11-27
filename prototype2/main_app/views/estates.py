# from django.template.context_processors import request
# from rest_framework.decorators import action
# from rest_framework.viewsets import ViewSet
# from rest_framework import status
# from rest_framework.response import Response
# from main_app.models import Estate
# from estate.serializer import EstateSerializer


# class EstateViewSet(ViewSet):
#     #queryset = Estate.objects.all()

#     def list(self,request):
#         serializer = EstateSerializer(Estate.objects.all(),many=True)
#         return Response(status=status.HTTP_200_OK,data = serializer.data)

#     def retrieve(self,request,pk:int):
#         serializer = EstateSerializer(Estate.objects.get(pk=pk))
#         return Response(status=status.HTTP_200_OK,data= serializer.data)

#     def create(self,request):
#         serializer = EstateSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
#     # decorador que valida que el id sea del dueño, token bobtener el id y validar
#     def update(self,request,pk:int):
#         serializer = EstateSerializer(instance=Estate.objects.get(pk=pk),data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

#     def partial_update(self,request,pk:int):
#         serializer = EstateSerializer(instance=Estate.objects.get(pk=pk),data=request.data,partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

#     def destroy(self,request,pk:int):
#         try:
#             product = Estate.objects.get(pk=pk)
#             product.delete()
#             return Response(status=status.HTTP_200_OK, data={pk: "eliminado"})
#         except Estate.DoesNotExist:
#             return Response(status=status.HTTP_200_OK, data={pk:"no existe"})

#     @action(detail=False, methods=['get'], url_path='owner/(?P<owner_id>[^/.]+)')
#     def estates_by_owner(self, request, owner_id):
#         estates = Estate.objects.filter(owner_id=owner_id)
#         serializer = EstateSerializer(estates, many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)



