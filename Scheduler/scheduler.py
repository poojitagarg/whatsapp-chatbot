from twilio_func import *
from datetime import datetime
from datetime import date
from datetime import time
import apscheduler
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dateutil.parser import parse

s=['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']
#p= parse(msg)
dt=date.today().strftime('%d/%m/%Y')
now_date=datetime.strptime(dt,'%d/%m/%Y')
rem_day=now_date.day
rem_month=now_date.month
rem_year=now_date.year

t=datetime(rem_year,rem_month,rem_day,19,46)
local = pytz.timezone("Asia/Kolkata")
local_dt = local.localize(t, is_dst=None)
utc_dt = local_dt.astimezone(pytz.utc)


scheduler = BlockingScheduler()
creds= ServiceAccountCredentials.from_json_keyfile_name("credentials.json",s)
client=gspread.authorize(creds)

#sheet = client.open("test")
worksheet = client.open("Reminders").sheet1
list_of_lists = worksheet.get_all_values()
print(list_of_lists)
for row in list_of_lists:
    #print(row[2])
    p= parse(row[0])
    print(p)
    pp=p.strftime('%d/%m/%Y')
    print(pp)
    print(dt)
    print(row[1])
    if pp == dt:
        scheduler.add_job(send_rem, 'date', run_date=utc_dt, args=[row[0],row[1]])
        print("yoyo")
    else:
        pass
        
scheduler.start()


