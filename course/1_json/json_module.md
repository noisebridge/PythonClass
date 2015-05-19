

#### An introduction to the JSON Module in Python


#### 0. Today's deep dive: Playing more with python's types and conversions (10 min)

please enter the python interactive interpreter: 
   ```python```

    ```python
    number_list = range(11)

    string_list = list()
    for num in number_list:
      string_list.append(str(num))

    print(string_list)
    print(number_list)

    string_list[:5]
    number_list[:-3]

    string_nums = '5' + '4'
    integer_conversion = int(string_nums)

    string_float = '3.25' + '1.02'
    float_conversion = float(string_float)
    ```

  a. where are these referenced in [the official python docs?](https://docs.python.org/2/library/index.html) 

#### 1. Review JSON format (20 min)

  a. http://www.json.org/    
  b. Values: string, number, object, array, true, false, null    
  c. Root Object must be a container: object, array


#### 2. Explain Python Data Types & Containers' relationship to JSON library (15 min) 

  a. Json to Python Standard Translation: https://docs.python.org/2/library/json.html#encoders-and-decoders     

#### 3. Sample JSON Request - Pull some data off a remote server using requests (15 min)

  a. What is requests? http://docs.python-requests.org/en/latest/    
  b. Use request to get a json encoded object. https://raw.githubusercontent.com/PyClass/PyClassLessons/master/lessons/json_module/examples/abcdef.json  
  c. Run through basic abilities of requests quickly - r.status, r.string, etc.    
  d. r.json() converts the data at the URL to python data types. Requests governs how this is done (probably uses json module).
  e. encoded_object_string = json.dumps(r.json()) will provide a string of the data.    


#### 4. Using json library functions: https://docs.python.org/2/library/json.html (20 min)
    
  a. Functions: load, dump, loads, dumps    
  b. loads and dumps are 'load string' and 'dump string'
  b. Quick Detour - The 'with' keyword - specifically for file objects.    
  ```python
    with open('stored_data.json', 'w') as f:        
        json.dump(r.json(), f)    
  ```
  d. Json load and loads will provide UTF-8 data, u'data', which is OK! Just treat it like a string without the u''    


5. Additional Resources

  a. Command line: $ python -m json.tool file.ext    
  b. Here's an example of json.loads() on a string variable: https://docs.python.org/2/library/json.html#repeated-names-within-an-object    
  c. Unicode characters (uXXXX): http://www.unicode.org/charts/    
  d. Duck Typing - http://en.wikipedia.org/wiki/Duck_typing    
  (don't explicly use types in your functions/checks)    

