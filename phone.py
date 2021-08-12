import phonenumbers
from phonenumbers import timezone
from phonenumbers import carrier
x=phonenumbers.parse("+254717xxxxx",None)
print(x)
print(phonenumbers.is_valid_number(x))
i=1
#while i<=10:
 #   num=input("tel :")
  #  formatter=phonenumbers.AsYouTypeFormatter("US")

num=input("what is your tel no: ")
y=num[1:10]
print(y)
z="+254"
w="{}{}".format(z,y)
print(w)
no=phonenumbers.parse(w)
print(timezone.time_zones_for_number(no))
print(carrier.name_for_number(no,"en"))
