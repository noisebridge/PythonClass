#### JSON, Unicode, and File Handling

This is a compressed lesson designed as a jumpstart for working with the open() built-in method, json encoding, unicode encoding, and the json module.


1. ##### Working with open() built-in method to access a file (50 minutes)

```bash
$ echo "hello world" > input.txt
```

```python
filename = 'input.txt'

f = open(filename)
contents = f.read()
f.close()

print(contents)
```

    1. What is going on here?

        1. First we create a variable to hold the filename as a string
        2. Next we pass that variable to the built-in Python `open` function
        3. We read out the contents of the file, and then `close` the file
        4. Finally we print out the contents

    2. Simplifying our code - 10 minutes

        The `close` step in the program is interesting.  Almost every file
        `open` should be followed by a corresponding file `close`.  Python
        provides us with a way to make this process slightly easier.  The
        program below is completely functionally equivalent:

```python
filename = 'input.txt'

with open(filename) as f:
    contents = f.read()

print(contents)
```

        1. Best practice - use `open` with the code pattern above, [with...as](https://docs.python.org/2/reference/compound_stmts.html#the-with-statement).
        2. The colon on line 3 indicates the beginning of a `code block`.  The
        file `f` is only open until we reach the end of the block.
        3. Take a look at the docs for
        [open][https://docs.python.org/2/library/functions.html#open]

    2. So, what [mode](https://docs.python.org/2/library/functions.html#open)s can we open a file in?
        1. 'r' - read mode. Read a file from the first byte. Cannot write.
        2. 'w' - delete the whole file and start writing from the first byte.
        3. 'a' - append a file starting at the last byte.
        4. 'rw' - read and write. be careful! if you read up to a point you can overwrite from there. This is challenging to use and you never really need it.
        5. 'b' - must be added on to 'r', 'w', probably 'a' in windows. It means binary mode. Files could be interacted with as binary or as bytes.
		6. Lets try using a file mode:

```python
filename = 'output.txt'

with open(filename, 'w') as f:
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

