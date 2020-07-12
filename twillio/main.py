import sms
import twillio_creds

sms.send_message(twillio_creds.jwl_num, "test_message")