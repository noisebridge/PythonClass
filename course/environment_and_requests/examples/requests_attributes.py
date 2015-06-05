import requests
from pprint import pprint as pp

#text based site with content on computer and programming topics
req = requests.get("http://slashdot.org/")

#pp(dir(req))

#pp(dir(req.text))

#pp(req.text.split())

#print req.close
#print req.close()

#print req.connection

#print req.content

#print req.cookies 

#print req.elapsed 

#print req.encoding 

##print (req.headers)
#below works better for dict objects
#for k, v in req.headers.items():
#    print k, ':', v 

#print req.history  

#print req.is_permanent_redirect

#print req.is_redirect 

#skipping req.iter_content() because this can result in infinite loop

"""multiple line strings are easier than multiple line comments sometimes 
itercontent_gen = req.iter_content()
for i in range(15):
    print itercontent_gen.next()

print 'done with itercontent_gen printing'

iterlines_gen = req.iter_lines()
for i in range(15):
    print iterlines_gen.next()
"""

#print req.json()

#print req.links

#print req.ok

#print req.raise_for_status()

#print req.raw 
#print dir(req.raw) 

#print req.reason #hmm HTTP keyword?

#print req.request  #prepared request object type

#print req.status_code

#print req.text #all

#print req.url