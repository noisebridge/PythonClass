##Functions!

1. What exactly is a function? (30 min)
  a. Options for what a function returns, what is that return statement doing?
  b. Exercise: demystify the print and return statements when do we get the None value. Final option is the yield keyword.
  c. Everyone should write functions that return different possible values
  d. Functions as first class-citizens?
    ie: Functions are just like the object type in that they can be assigned to variables, stored in collections or passed as arguments. Yes js, no c++ and java.
  e. Functions as methods
  f. Pass-by-value where all the values are references. Some languages pass copies of the objects to functions. Mutable v. immutable
     -[Knupp says it best](http://www.jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/)
  g. How to avoid "side-effects"


2. How functions function in your broader programs (20 min)
  a. Connecting that function with other results
  b. The scope of the variable within that function, using globals and locals or dir() to freeze-frame our environment, contrast with a slightly more functional style
  c. Scoping might include garbage collecting as well
  d. Exercise to pass some variables along from func to func
  e. As an aside may briefly mention lambdas anonymous functions, still syntactic sugar
  f. Could mention how to override functions as well



3. OPF - Other People's Functions: Documentation and Testing
  a. [Reading the Docs using learned conventions](https://docs.python.org/2/library/string.html#string-formatting) - search for nesting arguments and more complex examples after reading format API
  b. Why and how to document and ingenius function
  c. Most basic ways of testing your functions
  d. Ways of writing your functions accordingly


4. More advanced stuff worth digging into or dataset?
  a. Functions as objects and closures
  b. Peer into functools library
  c. Brief decorator and use case
  d. Generators and yield
  e. Didn't know about concept of function attributes and that they are stored in the __dict__ attribute