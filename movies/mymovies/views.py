from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'Index.html')

def tail(request):
    return render(request, 'tail.html')
