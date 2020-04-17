import datetime
import csv
import os
import Alarm_Notification_Sender
             
def main():
    
    path = os.getcwd() + "\\Data\\"
    alarms = []
    now = datetime.datetime.now()
    start = now - datetime.timedelta(seconds=2)
    end = now  
    
    try:
        with open((path + 'CNCAlarms')) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='\t', quotechar='"')
            firstline = True
        
            for row in csv_reader:
            
                if firstline:
                    firstline = False
            
                else:
                    date = datetime.datetime.strptime(str(row[1])[0:19],  "%Y-%m-%d %H:%M:%S")
                
                    if start <= date <= end:
                        Alarm_Notification_Sender.send_message([row[3], row[5]])
              
        with open((path + 'PMCAlarms')) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='\t', quotechar='"')
            firstline = True
            for row in csv_reader:
            
                if firstline:
                    firstline = False
            
                else:

                    date = datetime.datetime.strptime(str(row[1])[0:19],  "%Y-%m-%d %H:%M:%S")                
                    if start <= date <= end:
                        date = datetime.datetime.strptime(str(row[1])[0:19],  "%Y-%m-%d %H:%M:%S")
                        if row[4] == '190004' or row[4] == '210010':
                            Alarm_Notification_Sender.send_message([row[3], row[7]])  
    except:
        pass
    