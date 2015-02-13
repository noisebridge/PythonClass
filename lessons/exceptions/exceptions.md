
### Exceptions

Ten thousand foot view:  Exceptions are errors that occur when an application is running. If they 


### 0. Two major types of Error Messages - [Syntax Errors vs. Exceptions](https://docs.python.org/2/tutorial/errors.html)
- Syntax Errors === Parsing Errors (the 'grammar rules' of Python)
- Exceptions happen during runtime and can be captured safely and handled, and what we're focused on today
- The parser will catch Syntax Errors, your application can't run if those exist
- You can catch exceptions.  The rest of the course will be focused on catching and handling exceptions


### 1. Some facts:
- Exceptions are classes, following the 'object oriented' programming paradigm
- Object oriented note: when you catch an exception it is an object, which is instantiated from that class
- Almost all built-in exceptions inherit from a class called Exception
- If you make an exception, you should also inherit from the Exception class
- Lets look at the 'class hierarchy' [built-in exceptions](https://docs.python.org/2/library/exceptions.html#exception-hierarchy)


### 2. Handling Exceptions - Control Structures
- [Easy version of try,except](https://docs.python.org/2/tutorial/errors.html#handling-exceptions)
- Python reference manual (hard version) exception handling keywords: [try, except, (finally)](https://docs.python.org/2/reference/compound_stmts.html#the-try-statement), [with, as](https://docs.python.org/2/reference/compound_stmts.html#the-with-statement), [raise](https://docs.python.org/2/reference/simple_stmts.html#raise) (Advanced users: see the raise doc linked here)
- Control flow is going to be our tool for recording an exception and going on with life (or letting the app fail)
- Major point of exception control: handling data coming from outside your application
- Lets do some examples of these control structures: try... except, try... except... finally, with... as, making a with... as.




