from django.shortcuts import render
from .callingBS import big;

def index(request):
    context={
        "content":big(),
    }
    return render(request, 'page.html', context=context)

