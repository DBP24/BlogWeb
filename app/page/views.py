from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        'dato' : 'Diego Bonatti'
    }
    return render(request,'page/index.html',context)
