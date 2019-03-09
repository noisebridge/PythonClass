=== Welcome to the Noisebridge PyClass! ===

PyClass is an introductory Python course run by the Noisebridge community. It helps students solve common programming problems while learning the language.  Classes are held Mondays 7:00 - 9:00 PM in the 'Church' Classroom, and are mostly organized through [https://meetup.com/noisebridge Meetup].  If you have not been to Noisebridge before, please try to arrive 15 minutes early so that you can be introduced to the space.

=== Course Material ===
The course contains six lessons along with assorted guest lectures.  Each of the core classes covers a programming tool, from JSON in the first class to deploying a flask webapp in the last.  Each class also demonstrates an aspect of Python that makes it special, and when taken together they are a good baseline for effective programming in the language. The current list of classes is:

* Storing and transmitting information with JSON
* [https://github.com/jgarst/PythonClass/tree/master/course/strings Working with text data]
* Relational databases and SQL
* Performance and Big O notation
* Objects and Classes
* Web applications with Flask

The material for these is available on [https://github.com/jgarst/PythonClass/tree/master/course github].  The classes tend to move fast, but can be repeated and have references to related material in the notes.

The first three classes (JSON, text data, SQL) are suitable for anyone, but will be more difficult if you are not comfortable using python as a calculator.

    # importing libraries
    import time
    
    # printing and calling functions
    print(time.ctime())
    
    # variables and math
    calculation = (1 * 2 * 3) / 2  
    
    # strings
    print('I've done some math!', calculation)

* If you are comfortable this program, you will be comfortable with the class. <br \>
* If can understand understand what the program is doing, the class is a good fit for you, but might seem fast.
* If you do not have Python installed on your machine, you are invited to the class, but encouraged to arrange a time with the organizer to get started first.

The last three classes assume familiarity with loops, functions and collections.  If you are comfortable with the following program you will be comfortable with the class.

    frequency_dict = {}
    word = "noisebridge"
    
    for letter in word:
        times = frequency_dict.get(letter, 0)
        times += 1
        frequency_dict[letter] = times

=== Python Setup ===
We use Python 3, and encourage students to do the same.  The best way to install Python depends on your operating system, but there are good [https://realpython.com/installing-python/ online tutorials] for most cases.  The class uses Jupyter notebooks for slides and example code, but encourages students to run python from text files on their computers.  If you do not have a preferred way of editing programs, Python comes with a simple code editor called IDLE.

Python can be difficult to install. If you don't yet have a programming environment, you are encouraged to message the organizer and get help with setup.

If you want to attend class, but don't have Python installed, you can try it out with [http://repl.it/languages/Python3 repl.it].  This will allow you to follow along every class except the last one, which covers python projects and Flask.  We still recommend installing Python on your computer as soon as possible.

=== Helping out and getting additional help ===
PyClass runs on volunteer effort, and we would love to have your help keeping it it excellent!  The simplest and most appreciated contributions are examples of things you don't understand about Python, especially if they are succinct or easy to turn into problems that others can learn from.

We are always looking for more people to teach classes.  This is a great way to solidify your understanding, find new and exciting edge cases, and help others.  We welcome people teaching existing classes, or their own classes on the subjects they are most excited about.  Remember, the only thing that qualifies people to run PyClass is having enough enthusiasm to show up.

If you need help getting started, getting unstuck, or getting someone to look at your code we are happy to help!  There are usually office hours during the week, announced in the class, and designed to solve these problems.  Feel free to reach out over meetup to learn more.

=== Code of Conduct ===
PyClass holds to the Noisebridge [https://www.noisebridge.net/wiki/Community_Standards Community Standards], which we take seriously.

We also follow the Recurse Center [https://www.recurse.com/social-rules social rules], because they are excellent for creating a good learning environment.

=== Python Resources ===

For learning programming, we recommend that you consult multiple resources with a variety of formats and priorities.  Some of our favorite resources are <br />
-[http://learnpythonthehardway.org/ Learn Python the Hard Way] - A clear introduction to python intended for people new to programming.  Written well enough to be useful for more advanced programmers as well.  Available in the Noisebridge library. <br />
-[https://docs.python.org/3 Python Documentation] - The Python documentation is a well written and comprehensive reference.  It isn't a page turner, but should be one of your first stops when confused. <br /> 
-[http://pymotw.com/3/ Python Module of the Week] - Python comes with batteries included, but it can still be hard find the best tool among the hundreds of modules it provides.  Python Module of the Week walks you through each of the standard library modules provided by the language.  <br />
- [https://pyvideo.org/ pyvideo] - A searchable index of Python conference talks.  Drop by class for some specific recommendations! <br />
- [http://pythontutor.com/ python tutor] - pythontutor.com allows you to walk through small pieces of code and understand how Python thinks of them.  An excellent resource for debugging mysterious Python behavior.

There are more good resources for learning Python than we can list here.  Do you have a favorite that you think is missing?  Let us know!

=== Free to all - please donate to Noisebridge! ===

This course only happens because the Noisebridge community provides a space for it to exist.  Maintaining the space and broader community is difficult and thankless work.  The course is free, but if you want to help the community pay rent go to: https://www.noisebridge.net/wiki/Donate_or_Pay_Dues.  <br />
Recommended Donations: $15, $50, $200+ Recommended monthly donations: $10, $20, $40, $80+ / month
