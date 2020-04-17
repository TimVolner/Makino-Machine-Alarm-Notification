import smtplib

def machine(id):
    machines = ['', '', 'A61', '', '', '', '', 'A51-202', 'A51-808', '', '', '', ]
    return(machines[int(id)])

def send_message():
    DevID = 2
    TEXT = 'TEST'
    
    FROM = ''
    TO = '<TO EMAIL>'
    SUBJECT = 'TEST'

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

    try:
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo() # optional, called by login()
        server_ssl.login("<EMAIL>", '<PASS>')  
        # ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
        server_ssl.sendmail(FROM, TO, message)
        #server_ssl.quit()
        server_ssl.close()
        print("Successful")
      
    except:
        pass

send_message()