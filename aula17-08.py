import phonenumbers
from phonenumbers import geocodes, carrier

PhoneNumber = phonenumbers.parse('+55488988157712')
Carrier =  carrier.name_for_number(PhoneNumber, 'pt-br')