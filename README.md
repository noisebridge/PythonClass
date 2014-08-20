
### PSAs and Events

**PSA 8-19-14:** The [noisebridge wiki](https://noisebridge.net/wiki/PyClass) and [github readme](https://github.com/PyClass/PyClass-lesson-plans) files now have parity to each other.

**PSA 8-16-14:** The new curriculum for the Noisebridge PyClass is a crash course in the Python standard library, also touching on modules that are popular but not quite part of the standard modules. Scroll down to see the course list.

### Scheduled Weekly Meeting Times

* Tuesday 7:00 - 9:00 PM PST - 'Turing' Classroom
* Wednesday 7:00 - 9:00 PM PST - 'Church' Classroom

### Mailing List

Sign up for this to hear updates and conversations regarding the course!

[PyClass-Discussion](http://groups.google.com/group/pyclass)


### Class Description, Goals, and Ideal Student

The pace of the courses will be fast, and the materials will be available online 24/7 and we plan to frequently repeat modules that are in high demand with new twists as we iterate over the course materials.

A primary goal of the course is to break down the materials into independent units. In other words, if you miss a week then you won't fall behind. Sounds good, right?

To best experience the course, spend a short time studying the course materials before you come in. If you wish to know this week's courses, please send an email out to PyClass@googlegroups.com

The ideal student for this course can understand the following code (it's fine to use Google to look up the built in functions, and we use tons of web resources throughout the course materials):

```python
word_frequency_dict = {}
word = "noisebridge"
 
for letter in word:
    times = word_frequency_dict.get(letter, 0)
    times += 1
    word_frequency_dict.update( {letter : times} )
```

### Course List


The order of the following courses has not yet been determined.  

Please email PyClass@googlegroups.com if you want to know what courses are coming this week!

1. [JSON format, Python Types, and the JSON Module](https://github.com/PyClass/PyClass-lesson-plans/blob/master/1_json_module.md)    
2. Control Flow, itertools, and Functional Programming    
3. Built-in Functions    
4. Built-in Types and String Services    
5. Numeric and Mathematical Modules, and Operators    
6. argparse, ConfigParser, and more - configuring your applications    
7. pip, virtualenv, packaging, versions, and inspect.    
8. Logging your applications: logging, logging.config, logging.handlers    
9. Exceptions and Debugging: Exception behavior, custom exceptions, pdb, cProfile, timeit, time, trace.    
10. os, sys, and io (Caution, here be Python 3, inside the io module)    
11. (potential for a unittest course)    


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
