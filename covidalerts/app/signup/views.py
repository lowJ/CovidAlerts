from django.shortcuts import render
from django.http import HttpResponse
#from .forms import SignupForm
from . import forms
from signup.forms import SignupForm
from signup.data_processing import listcounties
from signup.phoneCheck import checkNumber, formatNumber
from signup.countyCheck import checkCounty



# Create your views here.
def home(request):
    if(request.method == "POST"):
        post_data = request.POST

        phone_num = post_data['phone_num']
        county_get = post_data['county']

        # check if phone number is valid
        phone_is_valid = checkNumber(phone_num)
        if phone_is_valid:
            phone_num = formatNumber(phone_num)

        # check if county is valid
        county_get = checkCounty(county_get)
        if type(county_get) is str:
            county_is_valid = False
        else:
            county_is_valid = True
            county, state = county_get

        if not county_is_valid:
            msg = county_get
        elif not phone_is_valid:
            msg = 'Invalid phone number.'
        elif 0: # need to check if phone num and county already exists in database
            msg = f'{phone_num} is already registered for {county_get} county.'
        else:
            msg = f'Successfully signed up {phone_num} to recieve alerts for {county}, {state}.'

        # msg = post_data['county'] + post_data['phone_num']
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
