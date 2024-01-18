from rest_framework import viewsets
from rest_framework.response import Response


class ExampleViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({"message": "GET request received via router"})

    def create(self, request):
        return Response({"message": "POST request received via router"})

    def update(self, request, pk=None):
        return Response({"message": "PUT request received via router"})

    def partial_update(self, request, pk=None):
        return Response({"message": "PATCH request received via router"})

    def destroy(self, request, pk=None):
        return Response({"message": "DELETE request received via router"})
