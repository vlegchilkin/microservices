from django.http import HttpResponse


# Function-based view
def function_view_1(request):
    return HttpResponse('function 1')


def function_view_2(request):
    return HttpResponse('function 2')
