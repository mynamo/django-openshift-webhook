from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('Hello World! We are all in this together :)')



