import requests
# using regex for pattern matching
import re


def numberinfo():
    # enter the phone number of which you want information
    number = input("Enter Mobile Number with country code : ")

    pattern = re.compile("^\+?(91)?[1-9][0-9]{9}")
    if pattern.match(number):
        # Use api to get the information of the number entered
        url = ("http://apilayer.net/api/validate?access_key=cd3af5f7d1897dc1707c47d05c3759fd&number=" + number)
        response = requests.get(url)

        # storing the content or result in details (here .json is used to retrieve the content)
        details = response.json()
        print('')
        print("Country : " + details['country_code'])
        print("Country : " + details['country_name'])
        print("Location : " + details['location'])
        print("Carrier : " + details['carrier'])
        print("Carrier : " + details['line_type'])
    else:
        print(f"{number} is not a valid number.")


if __name__ == "__main__":
    numberinfo()
