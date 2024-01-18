from django.urls import path

from different_urls_file_name.api.views import function_view_3, function_view_4

urlpatterns = [
    path('function-3/', function_view_3, name="function-3"),
    path('function-4/', function_view_4, name="function-4")
]