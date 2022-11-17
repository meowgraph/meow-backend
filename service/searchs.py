from django.http import HttpResponse


def search(request, content):
    return HttpResponse("Success")
