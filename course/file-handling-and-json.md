#### File Handling and JSON in Python

This lesson convers some of the basics of file input and output using Python,
as well as the popular JSON data encoding.


1. ##### Working with open() built-in method to access a file

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

2. Simplifying our code

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

1. Best practice - use `open` with the code pattern above,
[with...as](https://docs.python.org/2/reference/compound_stmts.html#the-with-statement).
This is called a 'context manager', and will ensure that the file is closed
even if your code encounters an exception.
2. The colon on line 3 indicates the beginning of a `code block` (also
used for `if` and `else` conditions).  The file `f` is only open until
we reach the end of the block.
3. Let's take a look at the docs for
[open][https://docs.python.org/2/library/functions.html#open]

2. So, what [modes](https://docs.python.org/2/library/functions.html#open) can we open a file in?
    1. `r` - read mode. Read a file from the first byte. Cannot write.
    2. `w` - delete the whole file and start writing from the first byte.
    3. `a` - append a file starting at the last byte.
    4. `rw` - read and write. be careful! if you read up to a point you can overwrite from there. This is challenging to use and you never really need it.
    5. `b` - the Windows platform considers text and binary files to be
    different, so we need to specify this if we are writing 'raw' bytes to a
    file on a Windows computer


Lets try using a file mode:

```python
filename = 'output.txt'

with open(filename, 'w') as f:
	f.write('The world is talking back to you.\n')
```

3. ##### Review JSON format and discuss Python types

JSON (JavaScript Object Notation) is a file format which can be used to store
and communicate data between computer systems, while still being (arguably)
readable by humans.  It's commonly used as a format for storing data in files
and for as a 'response' format for web APIs.

A JSON document describing some of the metadata about Noisebridge could be
written as:

```
{
    "address": "2169 Mission Street, San Francisco, CA",
    "name": "Noisebridge",
    "open": true,
    "members": ["a", "b", "c", ... ]
}
```

Note that JSON is a little stricter than Python with regards to quotation
marks and trailing commas; we always have to use double quotes for
fields/values, and we are not allowed trailing commas in lists or objects.

The full JSON format is specified at [json.org](http://www.json.org/) as a
[railroad diagram](https://en.wikipedia.org/wiki/Syntax_diagram).

Let's use a built-in Python tool to pretty-print some JSON data so that it's
more readable for us.

```json
{"url":"www.example.com","metadata":{"crawled_at":"2018-01-15","title":"Example Domain"}}
```

```bash
python -m json.tool example.json`
```

Python Data Types can be [encoded to to JSON (and back!)](https://docs.python.org/2/library/json.html#encoders-and-decoders)

This is called `encoding` and `decoding`. This allows complex data structures to exist easily as `flat` strings. It makes it easy to transport all this structure.

4. ##### Lets convert some JSON!

Two key actions are `encode` and `decode`. 

In the Python `json` module, these will be available as [`dump/load` and `dumps/loads`](https://docs.python.org/2/library/json.html#basic-usage)

Encoding and decoding is done by the json module. There are more details [here](https://docs.python.org/2/library/json.html#encoders-and-decoders).


###### Example: Using json.loads() and json.dumps()

```python
>>> import json
>>> help(json)
>>>
>>> my_json_string = u'{"message":"hello world"}'
>>> json.loads(my_json_string)
{u'message': u'hello world'}
>>>
>>> my_dict = json.loads(my_json_string)
>>> my_dict
{u'message': u'hello world'}
>>>
>>> json.dumps(my_dict)
'{"message": "hello world"}'
>>>
```

###### Exercise: Using json.load() and json.dump()

```python
"""
import json

data = {"message": "hello world"}

filename = 'data.json'

# write the data into the file data.json
# close the data.json file

# read the data back from data.json
# print the newly-read data and then close data.json
```
