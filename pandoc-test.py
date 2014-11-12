"""
print ra
Goal: Convert our markdown (.md) file to mediawiki format using pypandoc.


1. Get the file we want.
    a. Use requests to pull down the file.
    b. Get the file from request object as a string.
2. Convert the string to a mediawiki format with pypandoc. 
3. Store it in a file.

Stretch goals:
    Use requests.update or something like mechanize to put the file on noisebridge.net wiki.


"""


import requests
import pypandoc

target_url = "https://raw.githubusercontent.com/PyClass/PyClass-lesson-plans/master/README.md"
output_file = "README.wiki"

req_contents = requests.get(target_url)

text_contents = req_contents.text

output = pypandoc.convert(text_contents, 'mediawiki', format='md')

with open(output_file, 'wb') as f:
    f.write(output.encode('utf8'))



