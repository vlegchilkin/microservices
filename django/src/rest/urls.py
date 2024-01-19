from django.urls import path

from rest.views import ExampleViewSet, ListCreateView, RetrieveUpdateView, ExampleAPIView

urlpatterns = [
    # View set allows to provide mapping http method to python method
    path('viewset/', ExampleViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name="viewset-list"),

    # object id
    path('viewset/<int:pk>/', ExampleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name="viewset-detail"),

    # basic REST framework generic view (model based)
    path('custom-model/', ListCreateView.as_view(), name='custom-model-listcreate'),
    path('custom-model/<int:pk>/', RetrieveUpdateView.as_view(), name='custom-model-retrieveupdate'),
    # api view
    path('api-view/', ExampleAPIView.as_view(), name='api-view'),
]