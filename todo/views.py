from django.http import HttpResponse


# Create your views here.
def todo_view(request):
    response = HttpResponse('todo!')
    return response
