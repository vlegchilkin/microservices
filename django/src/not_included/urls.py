from django.urls import path

from not_included.views import not_included_function_view

urlpatterns = [
    # this urlpatterns is not included anywhere, so it should not be collected by endpoints
    path('should-not-be-present-in-endpoints/', not_included_function_view, name='should-not-be-present-in-endpoints'),
]
