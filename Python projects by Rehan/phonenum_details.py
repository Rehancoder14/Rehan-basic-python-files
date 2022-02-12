import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from phonenumbers import phonenumber

num = input("Enter Your Phone Number: ")
num_parse = phonenumbers.parse(num)
def get_timezone():
    time_zone =  timezone.time_zones_for_number(num_parse)
    print(f"The time zone of the phone number is {time_zone}")

def get_geocoder():
    geo_coder = geocoder.description_for_number(num_parse, "en")
    print(f"the geocode of the given number is {geo_coder}")
def get_carrier():
    carr_ier = carrier.name_for_number(num_parse, "en")
    print(f"The name of the carrier of phonenumber is {carr_ier} ")
def valid_possibility():
    checknum = phonenumbers.is_valid_number(num_parse)
    checkpossible = phonenumbers.is_possible_number(num_parse)
    print(f"{checknum} \n{checkpossible}")

get_timezone()
get_carrier()
get_geocoder()
valid_possibility()