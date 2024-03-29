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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import permission_required
from django.urls import path, include, re_path
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import settings
from .views import (
    function_view,
    function_view_for_regexp,
    function_view_with_if,
    function_view_with_decorator,
    ClassView,
    ClassViewWithDecorator,
    TemplateClassView, function_added_via_plus, function_added_via_extend, cached_view, required_post_view,
    view_csrf_exempt, view_permission_required
)

# See `app.settings.py` -> `ROOT_URLCONF`
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
    # Examples of wrapped views
    path('wrapped-view/cached-view', cache_page(10)(cached_view)),
    path('wrapped-view/require-post', require_POST(required_post_view)),
    path('wrapped-view/csrf_exempt', csrf_exempt(view_csrf_exempt)),
    path('wrapped-view/permission_required', permission_required('can_view')(view_permission_required)),

    # Included urls must be collected with `included_urls/` prefix
    path('included_urls/', include('included_urls.urls')),

    # The same as `included_urls` but URLs are defined in `api/endpoints.py`
    path('different_urls_file_name/', include('different_urls_file_name.api.endpoints')),

    # basic rest framework cases
    path('rest/', include('rest.urls')),

    # rest framework with router in urls.py
    path('rest-router/', include('rest_router.urls')),

    # Important urls with implementation provided by third party package
    # They should be present in endpoints
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += [
    path('added-via-plus', function_added_via_plus, name='added-via-plus')
]

urlpatterns.extend([
    path('added-via-extend', function_added_via_extend, name='added-via-plus')
])

# for serving django static files, like admin and rest-framework forms
# it is better to use nginx or so, but for this project it should be enough
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
