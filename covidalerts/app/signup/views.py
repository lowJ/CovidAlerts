from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    test_list= ['1', '2', '3', '4', '5', '6', '7']
    context = {
        'counties' : test_list
    }
    return render(request, 'signup/home.html', context)
