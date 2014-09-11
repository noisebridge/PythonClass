    
Python Regular Expressions - [The 're' module](https://docs.python.org/2/library/re.html)    
    
    
    
1. What are regular expressions?    
  a. [Regex HOWTO - Introduction](https://docs.python.org/2/howto/regex.html#regex-howto)    
  b. Compact, small language used to match strings.    
  c. regex can be [simple]() or [complex](http://stackoverflow.com/a/201378/1693693)    
    
2. What about in Python?    
  a. Regular expressions can parse 8-bit or unicode strings.    
  b. The backslash character escapes special characters in regular expression strings. Because backslash is also used to escape things in Python strings, it is better to use the raw string format r'<str>' for your regular expression string.    
  c. The re module uses regex objects.  There are a number of helper functions for simple cases.    
  d. [Regex HOWTO](https://docs.python.org/2/howto/regex.html#regex-howto) - Python is 'Perl Style'     
    
    
3. Lets do some regular expressions!    
  a. Compiling a string to a regex object using match/search/find/find (regex1.py). [Match vs. Search](https://docs.python.org/2/howto/regex.html#match-versus-search) As a general rule, if you can use search you should. This is for efficiency, so if you don't need efficency, do what you want. According to the docs, the re module is highly optimized.    
  b. Viewing the results stored in a match object (regex1.py    
  c. [Grouping](https://docs.python.org/2/howto/regex.html#grouping) - Extracting substring matches.    
  d. [Module level functions](https://docs.python.org/2/howto/regex.html#module-level-functions) - compilation is not always necessary, some general cases are precompiled.    
    
4. Things you should check out:    
  a. [Simple Patterns](https://docs.python.org/2/howto/regex.html#simple-patterns)    
  b. [Repeating Things](https://docs.python.org/2/howto/regex.html#repeating-things)    
  c. [Compilation Flags](https://docs.python.org/2/howto/regex.html#compilation-flags)    
  d. [More Metacharacters](https://docs.python.org/2/howto/regex.html#more-pattern-power)    
  e. [Modifying Strings](https://docs.python.org/2/howto/regex.html#modifying-strings) - Splitting Strings, Search and Replace     
  f. [Verbose, Readable REs](https://docs.python.org/2/howto/regex.html#modifying-strings)    
    
    
    
