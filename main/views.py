from django.shortcuts import render
from django import views
from django.http import HttpRequest, HttpResponse


# Create your views here.

class Main(views.View):

    template_name = 'main/app.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name=self.template_name)