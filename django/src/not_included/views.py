from django.http import HttpResponse


# This view is included in `not_included/urls.py`, but `not_included/urls.py` is not included anywhere.
# So, it is not possible to access that view.
def not_included_function_view(request):
    return HttpResponse('Hello, this is a function-based view')
