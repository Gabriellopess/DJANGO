from django.shortcuts import render

def index(request):
    context={
        'hello':'Hey folks! Welcome to my WebSite!',
        'compliments':'We are just gettin started...',
    }

    return render(request, 'core/index.html', context)
# Create your views here.
