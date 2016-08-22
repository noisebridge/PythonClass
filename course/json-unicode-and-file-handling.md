

#### JSON, Unicode, and File Handling

This is a compressed lesson designed as a jumpstart for working with the open() built-in method, json encoding, unicode encoding, and the json module.


1. ##### Today's deep dive: Opening a file (10 minutes)

    ```bash
    $ echo "hello world" > info.txt
    ```

    ```python
    myfile = 'info.txt'

    with open(myfile) as f:
        contents = f.read()

    print(contents)
    ```

    1. What is going on here? - 3 minutes
        1. First we save the filename as a 'string' variable in python
        2. Next we pass that filename through the open command
        3. But what the heck are the words 'with' and 'as' doing? This is a code pattern. More on this later.
    2. Reference Notes (self-teaching only)
        1. Why did we put print in parentheses? Do we have to? Should we?
        2. In what ways does this conform to PEP 8?


2. ##### Working with open() built-in method to access a file (50 minutes)

    1. The Python [open() built-in method](https://docs.python.org/2/library/functions.html#open)- 10 minutes
        1. Best practice - use this method in the code pattern above, [with...as](https://docs.python.org/2/reference/compound_stmts.html#the-with-statement).
        2. A `code pattern` is a `template` that you can copy whenever you need to do a similar thing.
        3. What about the colon? That's the beginning of a `code block`. That's an indented section that might run based on the [keyword](https://docs.python.org/2/library/keyword.html) before it.

    2. So, what [mode](https://docs.python.org/2/library/functions.html#open)s can we open a file in?
        1. 'r' - read mode. Read a file from the first byte. Cannot write.
        2. 'w' - delete the whole file and start writing from the first byte.
        3. 'a' - append a file starting at the last byte.
        4. 'rw' - read and write. be careful! if you read up to a point you can overwrite from there. This is challenging to use and you never really need it.
        5. 'b' - must be added on to 'r', 'w', probably 'a' in windows. It means binary mode. Files could be interacted with as binary or as bytes.
		6. Lets try using a file mode:
		```python

		myfile = 'info.txt'

		with open(myfile, 'w') as f:
			f.write('The world is talking back to you.\n')

		```

3. ##### Review JSON format and discuss Python types (30 min)

    1. [JavaScript Object Notation == JSON](http://www.json.org/)
        1. What is a [railroad diagram](https://en.wikipedia.org/wiki/Syntax_diagram)?
        2. The whole JSON 'piece' you are working with value must be a JSON value.
        3. Usually you will want this to be an OBJECT or ARRAY, since you want to have more than one piece of data.
        4. JSON Lint webapp can be used to check for valid JSON: [http://jsonlint.com/](http://jsonlint.com/)
        5. Side note: `python -m json.tool MYJSONFILE.json` on the command line will give you a human readable 'pretty looking' version. This is a tool contained in the json module.

    2. Python Data Types can be [encoded to to JSON (and back!)](https://docs.python.org/2/library/json.html#encoders-and-decoders)
        1. This is called `encoding` and `decoding`. This allows complex data structures to exist easily as `flat` strings. It makes it easy to transport all this structure.

4. ###### Lets convert some JSON!
    1. Two key actions are `encode` and `decode`. 
        1. In the Python `json` module, these will be available as [`dump/load` and `dumps/loads`](https://docs.python.org/2/library/json.html#basic-usage)
        2. Encoding and decoding is done by the json module. There are more details [here](https://docs.python.org/2/library/json.html#encoders-and-decoders).


    2. ###### Example 1: Using json.loads() and json.dumps()

        ``` Python
        >>>
        >>> import json
        >>>
        >>> dir()
        ['__builtins__', '__doc__', '__name__', '__package__', 'json']
        >>> dir(json)
        ['JSONDecoder', 'JSONEncoder', '__all__', '__author__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__', '__version__', '_default_decoder', '_default_encoder', 'decoder', 'dump', 'dumps', 'encoder', 'load', 'loads', 'scanner']
        >>>
        >>> my_json_string = u'{"5":"hello world"}'
        >>> json.loads(my_json_string)
        {u'5': u'hello world'}
        >>> my_dict = json.loads(my_json_string)
        >>> my_dict
        {u'5': u'hello world'}
        >>> json.dumps(my_dict)
        '{"5": "hello world"}'
        >>>
        ```

    3. ###### Example 2: Using json.load() and json.dump()

        ``` Python
        """
        These are where your notes go.

        Notes are good.

        Check out docstrings for more information.
        """
        import json

        my_json_dict = {"5":"hello world"}

        myfile = 'info.json'

        with open(myfile, 'w') as f:
            json.dump(my_json_dict, f)

        with open(myfile, 'r') as f:
            mydict = json.load(f)

        print mydict
        ```

