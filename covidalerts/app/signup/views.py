from django.shortcuts import render
from django.http import HttpResponse
#from .forms import SignupForm
from . import forms
from signup.forms import SignupForm
from signup.data_processing import listcounties

# Create your views here.
def home(request):
    if(request.method == "POST"):
        post_data = request.POST
        msg = post_data['county'] + post_data['phone_num']
        context = {
            'msg' : msg
        }
        return render(request, 'signup/success.html', context)
    
    counties_list = listcounties()
    form = forms.SignupForm(data_list=counties_list)
    context = {
        'counties' : counties_list,
        'form' : form
    }
    return render(request, 'signup/home.html', context)

