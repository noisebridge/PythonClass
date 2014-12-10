

Course 1 - An introduction to the JSON Module in Python


1. Review JSON format - 15 minutes

  a. http://www.json.org/    
  b. Values, Strings, Numbers, Arrays, Objects    
  c. Unicode characters (uXXXX): http://www.unicode.org/charts/    


2. Explain Python Data Types & Containers' relationship to JSON library 

  a. Python Interpreter - Fire it up and set (cat = 5) - 15 minutes    
  b. Duck Typing - http://en.wikipedia.org/wiki/Duck_typing    
  (don't explicly use types in your functions/checks)    
c. Json to Python Standard Translation: https://docs.python.org/2/library/json.html#encoders-and-decoders    



3. Sample JSON Request - Pull some data off a remote server using requests

  a. What is requests? http://docs.python-requests.org/en/latest/    
  b. Use request to get a json encoded object. https://raw.githubusercontent.com/PyClass/PyClass-lesson-plans/master/1_json_module/abcdef.json    
  c. Run through basic abilities of requests quickly - r.status, r.string, etc.    
  d. r.json() converts the data at the URL to python data types. Requests governs how this is done (probably uses json module).
  e. encoded_object_string = json.dumps(r.json()) will provide a string of the data.    


4. Using json library functions: https://docs.python.org/2/library/json.html
    
  a. Functions: load, dump, loads, dumps    
  b. loads and dumps are 'load string' and 'dump string'
  b. Quick Detour - The 'with' keyword - specifically for file objects.    
  ```python
    with open('stored_data.json', 'w') as f: #(make sure the file exists!)    
      json.dump(r.json(), f)    
  ```
  d. Json load and loads will provide UTF-8 data, u'data', which is OK! Just treat it like a string without the u''    


5. Additional Resources

  a. Command line: $ python -m json.tool file.ext    
  b. Here's an example of json.loads() on a string variable: https://docs.python.org/2/library/json.html#repeated-names-within-an-object    

