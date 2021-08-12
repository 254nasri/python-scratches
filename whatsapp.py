from twilio.rest import Client
acc='ACxxxxxxxxxxxxxxxxxx'
auth='10xxxxxxxxxxxxxxxxxx'
client=(acc,auth)

from_whatsapp_number='whatsapp:+14155238886'
to_whatsapp_number='whatsapp:+254717xxxxx'
msg='hello friend'
client.messages.create(body=msg,
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
