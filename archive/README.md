PyClass meets every Monday from 7 to 9 PM (PST) in the "Church" classroom.

The course is free! If you wish to donate, please give to [Noisebridge](https://donate.noisebridge.net).
- Recommended donations: $15, $50, $200+
- Recommended monthly donations: $10, $20, $40, $80+ / month

After class, we welcome your feedback! Submit the form [here](http://goo.gl/oMhxkv)

Contents:

- [Curriculum](#curriculum)
- [Course Description](#class-description-goals-and-ideal-student)
- [New Student Reading](#new-student-reading)
- [OS / Environment / Python Versions](#os--environment--versions)
- [Mailing List](#mailing-list)

### Curriculum
We usually run through a cycle of six core classes (below) over six weeks, then four weeks of guest talks, followed by an off week.

- [JSON and File Handling](course/file-handling-and-json)
- [String Methods and Usage](course/strings)
- [The Sqlite3 Database Library](course/sqlite3)
- [Writing an Algorithm](course/algorithms)
- [Functional Programming in Python](course/higher-order-functions)
- [Intro to Microservices with Flask](course/flask)

### Course Description, Goals, and Ideal Student
The course is designed with the following constraints in mind:
- The barrier to entry is low, but the pace is fast.
- All materials must be made [available on Github](https://github.com/PyClass/PyClassLessons).
- Each lesson stands alone, so it's okay to miss a week!
- The core, repeated modules are regularly updated.

To best experience the course, spend a short time reviewing the materials beforehand. If you wish to know what's scheduled for this week, please join [the mailing list](#mailing-list) and send an email out to PyClass@googlegroups.com

#### Prerequisites
Ideally, students starting the course can grasp the following code. Feel free to use web resources to look up anything you don't understand!

```python
letter_frequency_dict = {}
word = "noisebridge"

for letter in word:
    times = letter_frequency_dict.get(letter, 0)
    times += 1
    letter_frequency_dict[letter] = times
```

#### We use the [Socratic Method](http://www.criticalthinking.org/pages/socratic-teaching/606)
A Socratic questioner should

1. keep the discussion focused
2. keep the discussion fact-based\*
3. stimulate the discussion with probing questions
4. periodically summarize what has and what has not been dealt with and/or resolved
5. draw as many students as possible into the discussion.

\* [intellectually responsible](https://en.wikipedia.org/wiki/Intellectual_responsibility) can be effectively replaced with 'fact-based' for our needs.

### New Student Reading

#### Installing Python
For the sake of our sanity, we use Python 2 for this course.

Check out [The Hitchhiker’s Guide to Python!](http://docs.python-guide.org/en/latest/) for help installing Python, learning best practices, and finding useful packages. In an emergency, you can access Python [in your browser](http://repl.it/languages/Python).

#### Python Resources
If you are new to Python or to programming in general, here are some excellent resources:
- [The Official Python 2 Tutorial](https://docs.python.org/2/tutorial/)
- [Learn Python the Hardway](http://learnpythonthehardway.org/)
- [Byte of Python](http://www.swaroopch.com/notes/python/)
- [Learning Python, 5th edition](http://shop.oreilly.com/product/0636920028154.do) (Also available at the SF public library!)

Once you feel comfortable with the basics of the language, you can explore the standard library!
- [The Official Python 2 Documentation](https://docs.python.org/2/library/)
- [Python Module of the Week](http://pymotw.com/2/)

There are many, many good resources for learning the language of Python and how to do awesome things with it.
Those listed above are just a few based on personal experience and strong recommendations.

#### git
While git is worth learning in general, it will be particularly useful when trying to get the source code for each week's class. Installers are available for [Windows](http://git-scm.com/download/win) and [Mac](http://git-scm.com/download/mac), and Linux users can install via their package manager.

###  OS / Environment / Versions
We accept refugees using all operating systems. You will be politely prodded in the direction of solutions that are closer to [POSIX standards](http://en.wikipedia.org/wiki/POSIX#Mostly_POSIX-compliant).

Some options:
1. Use the command line in your Linux or Apple machine.
2. Install a Linux virtual machine on another computer using Virtualbox.
3. Explore [POSIX for windows](http://en.wikipedia.org/wiki/POSIX#POSIX_for_Windows)
4. Use a virtual private server (VPS).
    - [Digital Ocean $10 Credit](https://m.do.co/c/a4d54c9e5004) An easy way to get a free linux environment. If you are on Windows, you can login with [PuTTY](http://www.putty.org/).
    - Amazon's AWS has a [free tier](http://aws.amazon.com/free/) that allows you 750 compute hours every month of their t2.micro instances for 12 months.
        - Use EC2 to create an instance from the Ubuntu 16.04 AMI for the most well known and supported platform.

### Mailing List
Sign up for the [Noisebridge Python Mailing List](https://www.noisebridge.net/mailman/listinfo/python) to hear updates and conversations regarding the course!

The mailing list uses GNU Mailman and pipermail.  To search archives you may find it helpful to download the archive `.tar.gz` (compressed) file and use regular expressions (`grep`) to search.

The Python Class Google Group Closed on Tuesday, November 3rd, 2015.


### Other Resources
1. [Introductory Notebooks and Exercises](https://github.com/jerry-git/learn-python3)
