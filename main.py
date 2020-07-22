import sms
import db_interface
import data_processing


def helper(phone, state, county):

    r = data_processing.getday(state, county)
    if r is None:
        to_send = f"Could not find {county}, {state} in database."
    else:
        cases, deaths = r
        to_send = f"Todays confirmed cases in {county} {state}: " + str(cases) + " confirmed deaths: " + str(deaths)

    sms.send_message(phone, to_send)


db_interface.call_on_all_phone_num(helper)


