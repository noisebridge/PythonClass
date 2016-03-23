import requests


url = 'http://httpbin.org/post'
data = {'first_name': 'Mork', 'last_name': 'Cunningham'}

# submit post request
req = requests.post(url, data=data)

# display the response to screen
#print req.text
print req.content
print req.json



