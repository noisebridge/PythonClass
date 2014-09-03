Course 7 - Built-In functions, keywords and idioms    
    
    Resources for Sections:     
    -[The Docs!] (https://docs.python.org/2/library/functions.html)    
    -[Raymond Hettinger]: Anything he talks about but [this document](https://speakerdeck.com/pyconslides/transforming-code-into-beautiful-idiomatic-python-by-raymond-hettinger-1)    
    -Jeff Knupp: Writing Idiomatic Python - its a book    
    
    
    
Sections:    
    
1. About and why one should favor the built-ins - What is a namespace? (20 min)    
    a. A comprehensive view of what tools are given to us (https://docs.python.org/2/library/functions.html)    
    b. View these in interpreter environment using dir()    
    c. Interpreter: look even further with the help() function on the environment itself    
        -beware of the "modules" functionality!    
    
2. Taxonomy based on functionality and experience in application (20 min)    
    a. Discussion    
    b. How do we find the many arguments that these Built-ins might take?    
        -ie: round, sorted    
    c. Most commonly used    
    
3. Exercises (30 min)    
    a. create two lists, each with 20 numbers in them, the first where all numbers in list are     
    incremented by 10 the second incremented by 33    
    
    b. make an object 'paired-tup' that converts these two lists into one paired tuple object where each value in the first list corresponds with the other value in the other list. How many items are in this 'paired-tup' object    
    
    c. make another object 'paired-dict' that holds a converted version of the previous object into a dictionary where each paired tuple is now a key value in a dictionary. How many items are in that object?    
    
    d. make another object 'numbered' which takes the keys of 'paired-dict' and places them as the values in a dictionary, and the keys of 'numbered' are the indexes of the 'paired-dict' object. What type is this object?     
    
    e. reverse the order of the 'numbered' object by value    
    
4. List, Dict, and String methods, Tuple packing, Multiple Assignment    
    a. where to look up    
    b. commonly used    
    
5. List and Dict Exercises (10 min)    
    a. print all the keys in 'paired-dict'    
       print all the keys in 'paired-dict'    
       print all the items in 'paired-dict'    
    
    b. print all the keys in 'numbered'     
       print all the values in 'numbered'     
       print all the items in 'numbered'    
    
    c. add 10 to all the dicts values    
    
    assign the value "the first one" to the first item in the dict 'paired-dict'    
    
6. If time look more at Doc examples or Hettinger's slides    
    a. how to group with dictionaries    
    b. follow-up: magic methods    
    
    
