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
from django.urls import path, include, re_path

from .views import (
    function_view,
    function_view_for_regexp,
    function_view_with_if,
    function_view_with_decorator,
    ClassView,
    ClassViewWithDecorator,
    TemplateClassView
)

urlpatterns = [
    # URLs from the django library
    # Most likely they should not be collected by endpoints plugin
    path('admin/', admin.site.urls),

    # Basic views in Django directly imported here
    path('basic/function-view/', function_view, name="function_view"),
    # In very simple scenarios it is common to check for HTTP method using if
    path('basic/function-view-with-if/', function_view_with_if, name="function_view_with_if"),
    # Decorated with `login_required` which might affect endpoint collection
    path('basic/function-view-with-decorator/', function_view_with_decorator, name="function_view_with_decorator"),
    path('basic/class-view/', ClassView.as_view(), name="class_view"),
    # Decorated with `method_decorator` which might affect endpoint collection
    path('basic/class-view-with-decorator/', ClassViewWithDecorator.as_view(), name="class_view_with_decorator"),
    path('basic/template-class-view/', TemplateClassView.as_view(), name="template_class_view"),
    # Regexp url
    re_path(r'^basic/regexp-url/(?P<year>[0-9]{4})/$', function_view_for_regexp, name='function_view_for_regexp'),

    # Included urls must be collected with `included_urls/` prefix
    path('included_urls/', include('included_urls.urls')),

    # The same as `included_urls` but URLs are defined in `api/endpoints.py`
    path('different_urls_file_name/', include('different_urls_file_name.api.endpoints')),

    # basic rest framework cases
    path('rest/', include('rest.urls')),

    # rest framework with router in urls.py
    path('rest-router/', include('rest_router.urls')),
]