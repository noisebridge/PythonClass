import requests
from pprint import pprint as pp

url = "https://itunes.apple.com/search?term=Iron+Maiden"
url2 = "https://itunes.apple.com/search?term=Iron+Maiden&limit=5"
#payload = {"colors":None}


#headers = {"content-type": "application/json"}# post data to a web server
response = requests.post(url2)#, data=json.dumps(payload), headers=headers)

# output response to screen
#print response.status_code
pp(response.content)