import requests
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description='Send SHA1 value to a server.')
parser.add_argument('sha1', help='The SHA1 value to send')
args = parser.parse_args()

# URL of your server
url = 'http://mhaksserver.duckdns.org:5000/'

# SHA1 value to send in the request
sha1_value = args.sha1

# Payload for the POST request
payload = {'sha1': sha1_value}

# Send the POST request
response = requests.post(url, data=payload)
