import sms
import db_interface

import trung_function


#Code for scheudling text messages

#send at x:xx pm every day

def helper(phone, state, county):
    #trungs function
    data = trung_put_your_function_here(state, county):

    cases = data[0]
    deaths = data[1]
    to_send = "Todays confirmed cases: " + str(cases) + " conirmed deaths: " + str(deaths)
    sms.send_message(phone, to_send)


db_interface.call_on_all_phone_num(helper)