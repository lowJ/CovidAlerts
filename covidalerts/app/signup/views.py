from django.shortcuts import render
from django.http import HttpResponse
#from .forms import SignupForm
from . import forms
from signup.forms import SignupForm

# Create your views here.
def home(request):
    if(request.method == "POST"):
        form = SignupForm(request.POST)
        msg = request.POST
        context = {
            'msg' : msg
        }
        return render(request, 'signup/success.html', context)
    test_list= ['1', '2', '3', '4', '5', '6', '7']
    form = forms.SignupForm(data_list=test_list)
    context = {
        'counties' : test_list,
        'form' : form
    }
    return render(request, 'signup/home.html', context)

