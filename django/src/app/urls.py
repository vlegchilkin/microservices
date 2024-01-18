"""
URL configuration for djangoProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import (
    function_view,
    function_view_with_if,
    function_view_with_decorator,
    ClassView,
    ClassViewWithDecorator,
    TemplateClassView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basic/function-view/', function_view, name="function_view"),
    path('basic/function-view-with-if/', function_view_with_if, name="function_view_with_if"),
    path('basic/function-view-with-decorator/', function_view_with_decorator, name="function_view_with_decorator"),
    path('basic/class-view/', ClassView.as_view(), name="class_view"),
    path('basic/class-view-with-decorator/', ClassViewWithDecorator.as_view(), name="class_view_with_decorator"),
    path('basic/template-class-view/', TemplateClassView.as_view(), name="template_class_view"),

    path('included_urls/', include('included_urls.urls')),
]