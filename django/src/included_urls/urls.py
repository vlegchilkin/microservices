from django.urls import path

from included_urls.views import (
    function_view_1,
    function_view_2,
)

urlpatterns = [
    path('function-1/', function_view_1, name="function-1"),
    path('function-2/', function_view_2, name="function-2")
]
