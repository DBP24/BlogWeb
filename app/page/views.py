from django.shortcuts import render, HttpResponse

from .models import ProfessionalProfile as pp

# Create your views here.

def index(request):
    db = pp.objects.get()
    
    context = {
        'dato' : db
    }
    return render(request,'page/index.html',context)
