

#### Practical and ubiquitous Utilities in the stdlib    

##### datetime and os.path    

create a blank warmup.py in your favorite text editor    


1. #### Today's deep dive: Using the wheel rather than reinventing it (15 mins)
    

    ```python
    import datetime as dt
    from pprint import pprint

    #convert pprint.pprint callable into single letter if possible
    ```

    1. How does the [datetime module](https://docs.python.org/2/library/datetime.html?highlight=datetime#datetime.datetime) do what it does for us?
        1. What namespaces are we importing and not importing?
        2. How do we 'inspect' this module without importing the inspect module, ie: using builtins?
        3. Compare to documentation, how to read docs including signatures
    
2. #### What problems that this module is solving for us (10 mins)
    1. Concepts and terms to refer to those concepts   
        1. [The Unix Epoch](https://en.wikipedia.org/wiki/Unix_time) know epoch start date in datetime object
        2. Acronym soup: ISO, UTC, GMT, DST, locale
        3. Best post on what every dev should know about dates and times??? [maybe this one](http://blogs.windwardreports.com/davidt/2009/11/what-every-developer-should-know-about-time.html)
    2. Practical tools from docs    
        1. [strftime](https://docs.python.org/2/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior)    
        2. 
    3. Applying tools (30 mins)
        1. practical conversion problem 1: (1-prob_convert-and-print.py)
        2. much harder and less practical conversion problem 2: (2-prob_convert-and-json.py)    
        3. use regex to parse and convert to json for ultra win    
    4. Quickest detour into time and calendar modules in stdlib (10 min)    
        1. For the purpose of deciphering what functionality lives where in the stdlib    
        2. Also there are some neato and useful tricks see time-mod.py and calendar-mod.py in examples folder    
        3. For best and more full reference of time see: [Python Module of the Week!](http://pymotw.com/2/time/index.html#module-time)    
        4. Note: While time() returns a wall clock time, clock() returns processor clock time.    
        5. For best reference of calendar again see: [pymotw](http://pymotw.com/2/calendar/index.html#module-calendar)    
        6. pytz is widely used 3rd party modules for timezone    

3. #### os and os.path (30 mins)    
    1. What data do we have available to us now?      
        1. Let's play with the functionality in the [os.path module](https://docs.python.org/2/library/os.path.html?highlight=os.path#module-os.path)    
        2. What if we use the os.environ data?    
        3. os-path-walk.py is cool    
        4. more stuff to look at in nice print statements: os-example.py    
    2. Examples in popular python web development     
        1. example-django-envars.py    
        2. example-flask-envars.py[from flask mege-tut](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)    
        3. See: [example_file.py](example_file.py)
    3. Problem    
        1. 3-prob-newfile.py    


4. #### Extended Resources
    1. [SO question about conversions to weekday](http://stackoverflow.com/questions/9847213/which-day-of-week-given-a-date-python)    
    2. [pymotw - great supplement to docs for everything!](http://pymotw.com/2/contents.html)    
    3. [pycon talk about the problem of dealing with time](http://pyvideo.org/video/1765/blame-it-on-caesar-what-you-need-to-know-about-d)
