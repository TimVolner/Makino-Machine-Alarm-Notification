from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = '<Twilio_SID>'
auth_token = '<Twilio_auth>'
client = Client(account_sid, auth_token)

message = client.messages.create(
                     body="@ A51-202 --- Tool Life Alarm",
                     from_='<Phone_Number>',
                     to='<Phone_Number>'
                 )

print(message.sid, message.body)