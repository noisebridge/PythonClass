####Recursion and Classic Sorting Algos


#####Goals:    
-disambiguate and apply proper terms    
-iterate on a few select classic problems    
-provide additional tools and foundation for future complexities    

a. algorithm: a set of instructions used to produce a definitive result     or    
        -A step-by-step problem-solving procedure, especially an established, recursive computational procedure for solving a problem in a finite number of steps.    
b. data structure: a container for data with explicit features and/or restrictions

1. World of Data Structures and Algos: justification of lesson (15 min)    
    a. already using them all the time: implemented by language designers [doc](https://docs.python.org/2/tutorial/datastructures.html)       
    b. common / Uncommon use cases (ls_reimplementation.py, ls_operations_timed.py)    
    c. CS education / how to best learn this stuff [great official resource](http://interactivepython.org/courselib/static/pythonds/index.html)        
    d. interview questions: how to prep for each side, terminology, etc.    
    

2. Starting at high level: sum of all preceding numbers problem (sum_num.py) (20 min)    
    a. given a number, add all integers in between one and that number     
    b. understand with print statements and time module               


3. Recursion: Wait, why? ... Three rules (30 min)    
    -First: 'To understand recursion, you must understand recursion'     or      
    -'I have an inferiority complex, but it’s not a very good one' -Steven Wright   
    a. must establish a base case    
    b. must change state, moving towards the base case        
    c. must call itself recursively    
    d. re-implement sum of all preceding numbers / cleanest solution (recursum_fib.py)    
    e. who likes stories? [fibonacci problem](http://science.jrank.org/pages/2705/Fibonacci-Sequence-History.html) (recursum_fib.py)    
    f. [another fib](http://www.math.fau.edu/MathCircle_at_FAU/MC130713Problems.pdf)           
    

4. Binary search, Algo speak, and more Timeit (40 min)    
    a. algorithm: a set of instructions used to produce a definitive result     or    
        -A step-by-step problem-solving procedure, especially an established, recursive computational procedure for solving a problem in a finite number of steps.    
    b. data structure: a container for data with explicit features and/or restrictions    
    c. [big-O complexity chart](http://bigocheatsheet.com/) -(scroll to just above comment section)    
    d. [Big-O from the book](http://interactivepython.org/courselib/static/pythonds/AlgorithmAnalysis/BigONotation.html)    
    e. sequential search is stupid        
    f. design your own search algo in pseudocode: think about data and metadata    
    g. [binary sort](http://interactivepython.org/courselib/static/pythonds/SortSearch/TheBinarySearch.html) (sorting.py)    
    h. algo speak: analysis of binary search applying terms    
        [python lists from book](http://interactivepython.org/courselib/static/pythonds/AlgorithmAnalysis/Lists.html)    
        [python dicts from book](http://interactivepython.org/courselib/static/pythonds/AlgorithmAnalysis/Dictionaries.html)     

5. Merge Sort (30 min)    
    a. understand with print statements (sorting.py)    
        -[videos!](https://www.youtube.com/watch?v=GCae1WNvnZM)    
        -[from the book](http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html)    
    b. understanding and comparing to quick sort    
        -[more vids](https://www.youtube.com/watch?v=y_G9BkAm6B8)        

6. Recap / Interview Questions (40 min)    
    a. difference between merge sort and quick sort    
    b. when to use each / strengths and weaknesses of each    
    c. 


####Resources:
 [Great course in algos and data structures, interactive python style](http://interactivepython.org/courselib/static/pythonds/index.html)    
 [Coursera Course - graph heavy](https://www.coursera.org/course/algorithmicthink) called algorithmic thinking - uses python    
 others use java or are language agnostic