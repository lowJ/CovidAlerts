from django.shortcuts import render
from django.http import HttpResponse
#from .forms import SignupForm
from . import forms
from signup.forms import SignupForm
from signup.data_processing import listcounties
from signup.phoneCheck import checkNumber, formatNumber
from signup.countyCheck import checkCounty
from .db_interface import add_user, checkDuplicate



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
        elif checkDuplicate(phone_num, county, state): # need to check if phone num and county already exists in database
            msg = f'{phone_num} is already registered for {county} county.'
        else:
            add_user(phone_num, state, county)
            msg = f'Successfully signed up {phone_num} to recieve alerts for {county}, {state}.'

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
