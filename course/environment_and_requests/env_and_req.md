

#### Environment, Third Party Packages and Requests

0. #### Installation    
    1. Preferred Installations:    
        1. [Hitch Hiker's Guide to Python](http://docs.python-guide.org/) for best multiple platform guide to install python and virtualenv        
        2. [virtualenv](https://virtualenv.pypa.io/en/latest/) at read the docs    


1. #### Today's deep dive: Access to python code - 5 minutes    
    
    --what's diff between python interactive interpreter and writing a script in a .py file? 
    --when to use dir() and/or help() and when to go outside of these tools    

    ```python

    #for practice
    dir()
    dir(__builtins__)

    #std lib
    import json
    dir(json)
    help(json)

    ```

    1. References     
        1. [builtins documentation](https://docs.python.org/2/library/functions.html)    

2. #### The Standard Library: - 20 mins    
    1. [Python Library Reference](https://docs.python.org/2/library/index.html)    
    2. Builtin modules to have in your pocket  --   warning: Opinions!    
        a. builtins, json, sqlite3, datetime (and friends), random        
        b. pprint, csv, os, pdb, unittest    
    3. Builtin modules to know about before long    
        a. sys, collections, itertools, functools, timeit, futures        
        b. re, decimal (and math friends), string, copy     
    4. The long extra mile    
        a. knowing how import works, the future statement, and all the idioms    
        b. the [python 3 version of docs:](https://docs.python.org/3/reference/import.html)    
        c. [talk on how import works:](http://pyvideo.org/video/1707/how-import-works)    
        d. [lotsa fun with David Beazley:](http://pyvideo.org/video/3387/modules-and-packages-live-and-let-die) modules and packages - PyCon 2015    

    

3. #### Brief dive into the python environment, as in the language itself! - 20 minutes       
    1. Where on your computer are these things located?     
        1. in the virtualenv:      
        2. From python.org: [source code of 2.7.9](https://www.python.org/downloads/release/python-279/)    
        3. exploring the virtualenv a bit more: bin - include - lib and lib/site-packages    
    3. Who makes them and how are they controlled?    
        1. Software versioning in general, [PEPs](https://www.python.org/dev/peps/), Python 2 and 3 state of union    
            a. [HHG to python addresses this in writing](http://docs.python-guide.org/en/latest/starting/which-python/#the-state-of-python-2-vs-3)     


4. #### 3rd Party Packages and pypi - 15 mins    
    1. the cheeseshop aka [https://pypi.python.org/pypi](https://pypi.python.org/pypi)    
        a. what is pypi in the OOP paradigm? what type? what attributes?      
    2. 3rd party packages for your pocket    
        a. requests, basic ipython functionality     
    3. 3rd party packages to know before long or be aware of    
        a. flask, django, pandas, the entire sci-py ecosystem (mostly joking)    


5. #### Requests Library - 45 mins    
    1. [requests!](http://docs.python-requests.org/) http for humans    
        
