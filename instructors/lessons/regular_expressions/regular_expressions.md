    
#### Python Regular Expressions   

[Regular Expressions](http://en.wikipedia.org/wiki/Regular_expression) are sequences of characters symbolically used for matching strings and finding patterns. It comes in various 'flavors', with the most popular being 'perl flavor regular expressions'. You can use these in all different applications, and Python has a built in [regular expression module](https://docs.python.org/2/library/re.html)    
 in the Standard Library.


1. #### Installation and Class Prep
    1. Installation Instructions:
        1. The re module is part of the Python Standard Library, no installation required.
    2. Class Prep Resources:
        1. [The 're' module](https://docs.python.org/2/library/re.html)    



2. #### Today's deep dive: Special Characters (Regex Symbols)    

    1. [Special characters in Python regular expressions: .^$*+?\()| and more!](https://docs.python.org/2/library/re.html#regular-expression-syntax)


3. #### What are regular expressions?    
  1. [Regex HOWTO - Introduction](https://docs.python.org/2/howto/regex.html#regex-howto)    
  2. Compact, small language used to match strings.    
  3. regex can be simple (. simply means any one character) or [complex](http://stackoverflow.com/a/201378/1693693)    
  4. Special rules abound! In python, . will not match a newline unless you set the DOTALL flag.  Regular Expressions are part magic.

    
4. #### What about in Python?    
  1. Regular expressions can parse 8-bit or unicode strings.    
  2. The backslash character escapes special characters in regular expression strings. Because backslash is also used to escape things in Python strings, it is better to use the raw string format r'<str>' for your regular expression string. Raw strings don't need escaped.    
  3. [Regex HOWTO](https://docs.python.org/2/howto/regex.html#regex-howto) - Python is 'Perl Style'     
  4. This module creates objects for matches and provides helper methods for matches, searches, and other string comparison operations.    
    
    
5. #### Lets do some regular expressions!    
  1. Compiling a string to a regex object using match/search/find/findall. [Match vs. Search](https://docs.python.org/2/howto/regex.html#match-versus-search) As a general rule, if you can use search you should. This is for efficiency, so if you don't need efficency, do what you want. According to the docs, the re module is highly optimize4.    
  2. Example: regex1.py - viewing the results stored in a match object    
  3. [Grouping](https://docs.python.org/2/howto/regex.html#grouping) - Extracting substring matches.    
  4. [Module level functions](https://docs.python.org/2/howto/regex.html#module-level-functions) - compilation is not always necessary, some general cases are precompile4.    
  5. Continuing through regex2.py, regex3.py
    
6. #### We're not done yet! Now it's time to put all this hard work to good use.
  1. We want to organize our mp3 file library, which has a lot of classics from 'the beatles. Or was it The-beatles? Wow, looks like we also have 'theBeatles' in these filenames...
  2. Shoot, it looks like a lot of different people used similar patterns. This sounds like a job for regular expressions!


7. #### Extended Resources: Things you should check out from the 're' module standard library documentation:    

  1. [Simple Patterns](https://docs.python.org/2/howto/regex.html#simple-patterns)    
  2. [Repeating Things](https://docs.python.org/2/howto/regex.html#repeating-things)    
  3. [Compilation Flags](https://docs.python.org/2/howto/regex.html#compilation-flags)    
  4. [More Metacharacters](https://docs.python.org/2/howto/regex.html#more-pattern-power)    
  5. [Modifying Strings](https://docs.python.org/2/howto/regex.html#modifying-strings) - Splitting Strings, Search and Replace     
  6. [Verbose, Readable REs](https://docs.python.org/2/howto/regex.html#modifying-strings)    
    


