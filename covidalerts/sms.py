from twilio.rest import Client
import twillio_creds

account_sid = twillio_creds.twillio_acc_sid
auth_token = twillio_creds.twillio_auth

def send_message(num, msg):
    client = Client(account_sid, auth_token)

    print(num)
    client.api.account.messages.create(
        to="+" + num,
        from_="+17865634906",
        body=msg)

