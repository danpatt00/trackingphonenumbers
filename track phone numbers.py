import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Enter Mobile Number with country code: ")
MobileNo = phonenumbers.parse(mobileNo)

# get timezone a phone number
print(timezone.time_zone_for_number(mobileNo))

# Getting carrier of a phone number
print(carrier.name_for_number(mobileNo, "en"))

# Getting region information
print(geocoder.description_for_number(mobileNo, "en"))

# Validating phone number
print("Valid Mobile Number : ", phonenumbers.is_vailidnumber(mobileNo))

# Checking possibility of a number
print("Checking possibility of Number :", phonenumbers.is_possible_number(mobileNo))