from pprint import pprint
import random

import requests

MASTODON_HOST = 'https://mastodon.social'
MASTODON_TOKEN = 'dv2DCBcBpxcl1ceenbv6-KhL3a3ICOrjiHY_XmUgPJ0'

def post_to_mastodon(text):
    data = {'status': text}

    url = '%s/api/v1/statuses' % MASTODON_HOST
    r = requests.post(url, 
                      data=data, 
                      headers={'Authorization': 'Bearer %s' % MASTODON_TOKEN})
    return r.json()

with open('proverbs.txt', 'r') as file:
    text = file.read()
proverbs = text.split('\n')

post_to_mastodon(random.choice(proverbs))