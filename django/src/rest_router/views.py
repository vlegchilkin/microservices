from rest_framework import viewsets
from rest_framework.decorators import action
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


class ExampleViewSetOnActions(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def set_password(self, request, pk=None):
        return Response({'status': 'password set'})

    # detailed=True which means that `pk` will be parsed from url
    @action(detail=True, methods=['get'])
    def set_password(self, request, pk=None):
        return Response({'status': f'password set for {pk}'})

    @action(detail=False, methods=['get'], url_path='set-password-custom-path')
    def set_password_2(self, request, pk=None):
        return Response({'status': 'password set 2'})
