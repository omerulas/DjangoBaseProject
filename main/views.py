from django.shortcuts import render
from django import views

# Create your views here.

class Main(views.View):

    template_name = 'main/app.html'

    def get(self, request):
        return render(request=request, template_name=self.template_name)