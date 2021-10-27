
from twilio.rest import Client
 
account_sid = 'AC213eaf268eb24a22df790ac6ca3ed1bd'
auth_token = '04de4b2f6ae223388244838150c3019d'
client = Client(account_sid, auth_token)
def send_rem(date,rem):
    message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body='*REMINDER* '+date+'\n'+rem,
                                  to='whatsapp:+917696076160'
                              )
     
    print(message.sid)
