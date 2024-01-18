from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from rest.models import CustomModel
from rest.serializers import CustomModelSerializer


# GET POST PUT PATCH DELETE
class ExampleAPIView(APIView):
    def get(self, request, format=None):
        return Response({"message": "GET request received"})

    def post(self, request, format=None):
        return Response({"message": "POST request received"})

    def put(self, request, format=None):
        return Response({"message": "PUT request received"})

    def patch(self, request, format=None):
        return Response({"message": "PATCH request received"})

    def delete(self, request, format=None):
        return Response({"message": "DELETE request received"})


# GET POST         (HEAD OPTIONS)
class ListCreateView(generics.ListCreateAPIView):
    queryset = CustomModel.objects.all()
    serializer_class = CustomModelSerializer


# GET PUT PATCH    (HEAD OPTIONS)
class RetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = CustomModel.objects.all()
    serializer_class = CustomModelSerializer


# GET POST PUT PATCH DELETE (HEAD OPTIONS)
class ExampleViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({"message": "ListView request received"})

    def create(self, request):
        return Response({"message": "CreateView request received"})

    def retrieve(self, request, pk=None):
        return Response({"message": "RetrieveView request received"})

    def update(self, request, pk=None):
        return Response({"message": "UpdateView request received"})

    def partial_update(self, request, pk=None):
        return Response({"message": "Partial UpdateView request received"})

    def destroy(self, request, pk=None):
        return Response({"message": "DestroyView request received"})
