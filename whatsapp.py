from twilio.rest import Client
acc='AC123f01fc6e1258e668945157143d6156'
auth='1001bd2bbdbc6eba006ced26920f934a'
client=(acc,auth)

from_whatsapp_number='whatsapp:+14155238886'
to_whatsapp_number='whatsapp:+254717902628'
msg='hello friend'
client.messages.create(body=msg,
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)