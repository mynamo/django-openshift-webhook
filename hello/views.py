from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('Hello my fellow OpenShift enthusiast!')



