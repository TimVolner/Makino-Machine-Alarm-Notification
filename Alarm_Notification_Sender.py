from twilio.rest import Client

def machine(id):
    machines = ['', '', 'A61', '', '', '', '', 'A51-202', 'A51-808', '', '', '', ]
    return(machines[int(id)])

def send_message(alarm):
    DevID, TEXT = alarm
    
    FROM = '<PhoneNumber>'
    TO = ['<PhoneNumber>', '<PhoneNumber>', '<PhoneNumber>']
    subject = machine(DevID)
    
    
    # Prepare actual message
    message = "@" + subject + " --- " + TEXT

    account_sid = '<TwilioSID>'
    auth_token = '<TwilioAUTH>'
    client = Client(account_sid, auth_token)

    for person in TO:
        message = client.messages.create(
            body=message,
            from_=FROM,
            to=person
        )      