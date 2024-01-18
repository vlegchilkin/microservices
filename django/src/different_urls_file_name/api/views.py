from django.http import HttpResponse


# Function-based view
def function_view_3(request):
    return HttpResponse('function 3')


def function_view_4(request):
    return HttpResponse('function 4')
