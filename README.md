
### PSAs and Events

**PSA 10-1-14:** PyClass starts at 700 PM, try to come a few minutes earlier. We want to finish up by nine so people can hack or catch their preferred train home.  You can come at any time, but YMMV.

**PSA 8-19-14:** The [noisebridge wiki](https://noisebridge.net/wiki/PyClass) and [github readme](https://github.com/PyClass/PyClass-lesson-plans) files have the same information and updates.

**PSA 8-16-14:** The new curriculum for the Noisebridge PyClass is a crash course in the Python standard library, also touching on modules that are popular but not quite part of the standard modules. Scroll down to see the course list.

### Scheduled Weekly Meeting Times

We set up the space at 6:45 PM - try to arrive early to help if you are able to.

* Tuesday 7:00 - 9:00 PM PST - 'Turing' Classroom
* Wednesday 7:00 - 9:00 PM PST - 'Church' Classroom

### Mailing List

Sign up for this to hear updates and conversations regarding the course!

[PyClass-Discussion](http://groups.google.com/group/pyclass)


### Class Description, Goals, and Ideal Student

The pace of the courses will be fast, and the materials will be available online 24/7. We plan to frequently repeat modules with new twists as we iterate over course materials.

A major PyClass goal is to break down the courses into independent units. In other words, you won't fall behind if you miss a week. Sounds good, right?

To best experience the course, spend a short time reviewing the course materials before you come in. If you wish to know this week's courses, please join the mailing list and send an email out to PyClass@googlegroups.com

The ideal student for this course can grasp the following code (feel free to use web resources to look up anything you don't understand):

```python
letter_frequency_dict = {}
word = "noisebridge"
 
for letter in word:
    times = letter_frequency_dict.get(letter, 0)
    times += 1
    letter_frequency_dict[letter] = times
```

If you are new to python or programming in general here are some excellent resources:    
-[Learn Python the Hardway](http://learnpythonthehardway.org/) - great guide for total beginner    
-[Byte of Python](http://www.swaroopch.com/notes/python/) - nice guide for total beginner and new to python    
-[Excellent Official Python Tutorial - 2.7.8](https://docs.python.org/2/tutorial/) - great for new to python    
-[Learning Python 5th edition (also at sf lib)](http://shop.oreilly.com/product/0636920028154.do) - A comprehensive guide to the language and its uses    
-[Python Module of the Week](http://pymotw.com/2/) - Learning the standard library by example    
-[The docs themselves! 2.x for this class](https://www.python.org/doc/) - Learn what is and how to use the standard library

There are many, many good resources for learning the language of Python and how to do awesome things with it.
Those listed above are just a few based on personal experience and strong recommendations.  

### Course List


The order of the following courses has not yet been determined.  

Please email PyClass@googlegroups.com if you want to know what courses are coming this week!

1. [JSON format, Python Types, and the JSON Module](https://github.com/PyClass/PyClass-lesson-plans/blob/master/1_json_module.md)    
2. [Control Flow and Exceptions](https://github.com/PyClass/PyClass-lesson-plans/blob/master/5_control_statements.md)     
3. [itertools, and Functional Programming](https://github.com/PyClass/PyClass-lesson-plans/blob/master/3_functional_and_control.md)    
4. [Built-in Types and String Services](https://github.com/PyClass/PyClass-lesson-plans/blob/master/4_builtintypes_stringservices.md)    
5. 
6. 
7. 
8. 
9. 
10.
11.
12.
13.
14. [Unit Testing](https://github.com/PyClass/PyClass-lesson-plans/blob/master/14_unittest.md) - Exploring assert and python's builtin unittest module.







5. Numeric and Mathematical Modules, and Operators    
6. argparse, ConfigParser, and more - configuring your applications    
7. pip, virtualenv, packaging, versions, and inspect.    
8. Logging your applications: logging, logging.config, logging.handlers    
9. Exceptions and Debugging: Exception behavior, custom exceptions, pdb, cProfile, timeit, time, trace.    
10. os, sys, and io (Caution, here be Python 3, inside the io module)    
11. (potential for a unittest course)    
12. Built-in Functions    


###  OS / Environment / Versions

This section is under development.

For the sake of our sanity we use Python 2.7.1+ for this course.

Installing Python with [The Hitchhiker’s Guide to Python!](http://docs.python-guide.org/en/latest/)

Emergency Python Command Line: [http://repl.it/languages/Python](http://repl.it/languages/Python)


**We accept refugees using all operating systems. You will be politely prodded in the direction of solutions that are closer to posix standards: [http://en.wikipedia.org/wiki/POSIX#Mostly_POSIX-compliant](http://en.wikipedia.org/wiki/POSIX#Mostly_POSIX-compliant)**


Some routes:    
1. Install a linux virtual machine on another computer using virtualbox.    
2. Use the command line in your apple machine.    
3. Explore POSIX for windows: http://en.wikipedia.org/wiki/POSIX#POSIX_for_Windows    
    

Another critical tool is git:    
*Windows: http://git-scm.com/download/win    
*Mac: http://git-scm.com/download/mac    
*Linux: (use your package manager)    



###For Lesson Planners:

####Some Modules to include

* Control Structures, itertools - Teddy    
* requests    
* urllib/urllib2    
* math    
* ConfigParser    
* argparse    
* json    
* csv    
* time, datetime    
* os    
* sys    
* io    
* logging    
* decorators    
* Profile    
* subprocess (catchall replacement for system call libraries)    
* pdb    
* unittest    
* py.test    
* virtualenv    
* pip    
* packaging?    
* versions    



####Two approaches for course material building that should be blended

1. Modules Course - http://pymotw.com/2
2. Applications Course - http://newcoder.io/dataviz/part-0/
