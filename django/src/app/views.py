from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


# Function-based view
def function_view(request):
    return HttpResponse('Hello, this is a function-based view')


def function_view_with_if(request):
    if request.method == 'GET':
        return HttpResponse('You performed a GET request on function-based view')
    if request.method == 'POST':
        return HttpResponse('You performed a POST request on function-based view')


# Function-based view with a decorator
@login_required
def function_view_with_decorator(request):
    return HttpResponse('Hello, this is a function-based view with a login_required decorator')


# Class-based view
class ClassView(View):
    def get(self, request):
        return HttpResponse('Hello, this is a class-based view with a GET request')

    def post(self, request):
        return HttpResponse('Hello, this is a class-based view with a POST request')


# Class-based view with a method decorator
@method_decorator(staff_member_required, name='dispatch')
class ClassViewWithDecorator(View):
    def get(self, request):
        return HttpResponse('Hello, this is a class-based view with a staff_member_required decorator')


# TemplateView
class TemplateClassView(TemplateView):
    template_name = "template_name.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variable'] = 'value'
        return context
