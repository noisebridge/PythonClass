OOP, Classes and Class interaction  

spike: what OOP isn't   
let’s open up our good friend [repl.it](http://repl.it/) and [Scheme](https://classes.soe.ucsc.edu/cmps112/Spring03/languages/scheme/SchemeTutorialA.html) some non-OOP     
    starting with a couple built-in functions   
    (print "Hello, " (read) "!")
    now let's define some of our variabls   
    (define pi 3.14)
    (define square (lambda (x)  (* x x)))

    (define my_list (list 1 2 3 5))

    (define length
           (lambda (l)
                   (if (null? l)
                          0
                          (+ 1 (length (cdr l))))))