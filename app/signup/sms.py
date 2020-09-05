from twilio.rest import Client
import twillio_creds

account_sid = twillio_creds.twillio_acc_sid
auth_token = twillio_creds.twillio_auth

def send_message(num, msg):
    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to="+1" + num,
        from_="+" + twillio_creds.from_number,
        body=msg)