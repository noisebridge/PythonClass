
Hanlon's Razor - Noisebridge Discussion Boards



Course 1 - An introduction to the JSON Module in Python


1. Review JSON format - 15 minutes

  a. http://www.json.org/    
  b. Values, Strings, Numbers, Arrays, Objects    



2. Explain Python Data Types & Containers' relationship to JSON library 

  a. Python Interpreter - Fire it up and set (cat = 5) - 15 minutes    
  b. Duck Typing - http://en.wikipedia.org/wiki/Duck_typing    
  (don't explicly use types in your functions/checks)    
c. Json to Python Standard Translation: https://docs.python.org/2/library/json.html#encoders-and-decoders    



3. Sample JSON Request - Pull some data off a remote server using requests

  a. What is requests? http://docs.python-requests.org/en/latest/    
  b. Use request to get a json encoded object.    
  c. Start manipulating it with relevant json library functions.    
  d. encoded_object_dict = json.load(r.json()) will provide a dictionary of the encoded data.    



(might not include this detour)
4. Quick Detour: Opening and Closing files:
    
  a. The 'with' keyword - specifically for (io/files/something).    
  b. with open('filename.ext', 'r') as f:    
      json_object = json.load(f)    


5. Using json library functions: https://docs.python.org/2/library/json.html

a. Functions: load, dump, loads, dumps    
b. Json load and loads will provide UTF-8 data, u'data', which is OK! Just treat it like a string without the u''    
c. Command line: $ python -m json.tool file.ext    
d. Here's an example of json.loads() on a string variable: https://docs.python.org/2/library/json.html#repeated-names-within-an-object    


