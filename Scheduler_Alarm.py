import schedule
import time
import os
import SQL_Reader_AlarmSystem, Alarm_Notification


def job():
    try:
        SQL_Reader_AlarmSystem.main()
        Alarm_Notification.main()
    except:
        pass
    
def main():
    schedule.every(2).seconds.do(job)

    while True:
        schedule.run_pending()
        
main()