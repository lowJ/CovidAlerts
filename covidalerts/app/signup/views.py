from django.shortcuts import render
from django.http import HttpResponse
#from .forms import SignupForm
from . import forms
from signup.forms import SignupForm
from signup.data_processing import listcounties
from phoneCheck import checkNumber, formatNumber
from countyCheck import checkCounty



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
    
    #Still figuring out where this should go
    """
    #Check if phone number is valid
    if checkNumber(post_data['phone_num']):
        post_data['phone_num'] = formatNumber(post_data['phone_num'])
       
    #check if county is valid
        county_get = checkCounty(county_get)
        if type(county_get) is str:
            county_is_valid = False
        else:
            county_is_valid = True
            county, state = county_get
    """
