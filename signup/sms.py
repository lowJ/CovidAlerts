from twilio.rest import Client
import creds

account_sid = creds.twillio_acc_sid
auth_token = creds.twillio_auth

def send_message(num, msg):
    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to="+1" + num,
        from_="+" + creds.from_number,
        body=msg)