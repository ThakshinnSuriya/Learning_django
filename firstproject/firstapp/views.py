from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
def hello_world(request):
    return httpResponse("Hello, World!")

class hello(View):
    def get(self, request):
        return HttpResponse("Hello, World from Class-Based View!")
    
    

