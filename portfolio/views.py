from django.shortcuts import render

# Create your views here.
from portfolio.models import Project #asi se tiene que importar de manera correcta un modelo


def home(request):
   projects = Project.objects.all() #esta variable almacena todos los proyectos del objeto
   return render(request, 'home.html',{'projects':projects})