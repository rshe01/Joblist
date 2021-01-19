from django.shortcuts import render
from .bs import bs;

def index(request):
    context={
        "content":bs("https://www.indeed.com/jobs?q=Computer+Science+Internship"),
        "loopLength":range(15),
    }
    return render(request, 'page.html', context=context)

