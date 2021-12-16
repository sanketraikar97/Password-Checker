# Password Checker
import sys

import requests  # it allows us to make a request manually
import hashlib  # it allows us to perform hashing algorithms
import re  # it allows us to match password pattern using regular expression

# Global data Declaration
hack_count = 0
password = ''


# Function to request api data
def fetch_api_data(sct_str):
    url = 'https://api.pwnedpasswords.com/range/' + sct_str
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'error fetching data response: {response.status_code}')
    return response


# Check if password exists in API database
def check_pwned_api(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1_hash[:5], sha1_hash[5:]
    res = fetch_api_data(first5)
    return get_leak_count(res, tail)


# Get all the tail strings & count of hacks that match the first5 characters of the SHA1 hash
def get_leak_count(hashes, check_hash):
    #     print(hashes.text)
    hash_tail = (line.split(':') for line in hashes.text.splitlines())
    # print(hash_tail)
    count = 0
    for entry in hash_tail:
        if entry[0] != check_hash:
            continue
        else:
            count = int(entry[1])
            # print(count)
            break
    return count


def match_password_pattern(password):
    pattern = re.compile(r"([a-zA-Z0-9$%#@]{7,}\d$)")
    if re.match(pattern, password):
        print('It is a valid password')
        hack_count = check_pwned_api(password)
        display_data(hack_count)
    else:
        print('It is not a valid password')


# Display the info related to password
def display_data(hack_count):
    if hack_count > 0:
        print(f"Your password {password} has been hacked {hack_count} times. Please choose a different password")
    else:
        print(f"Your password {password} has not been hacked at all. U can use this password")


# password=input("Enter a Password: ")
password = sys.argv[1]
match_password_pattern(password)
