PyClass meets every Monday from 7 to 9 PM (PST) in the 'Church' classroom.
The course is entirely free, but [Noisebridge](https://donate.noisebridge.net) runs entirely on donations.

### PSAs and Events
TBD

### Class Description, Goals, and Ideal Student
The course is designed with the following constraints in mind:
- The barrier to entry is low, but the pace is fast.
- All materials must be made [available on Github](https://github.com/PyClass/PyClassLessons).
- Each lesson stands alone, so it's okay to miss a week!
- The core, repeated modules are regularly updated.

To best experience the course, spend a short time reviewing the course materials before you come in. If you wish to know what's scheduled for this week, please join [the mailing list](#mailing-list) and send an email out to PyClass@googlegroups.com

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
2. keep the discussion fact based\*
3. stimulate the discussion with probing questions
4. periodically summarize what has and what has not been dealt with and/or resolved
5. draw as many students as possible into the discussion.

\* [intellectually responsible](https://en.wikipedia.org/wiki/Intellectual_responsibility) can be effectively replaced with 'fact based' for our needs.

### New Student Reading

If you are new to python or programming in general here are some excellent resources:
- [Learn Python the Hardway](http://learnpythonthehardway.org/) - great guide for total beginner
- [Byte of Python](http://www.swaroopch.com/notes/python/) - nice guide for total beginner and new to python
- [Excellent Official Python Tutorial - 2.7.8](https://docs.python.org/2/tutorial/) - great for new to python
- [Learning Python 5th edition (also at sf lib)](http://shop.oreilly.com/product/0636920028154.do) - A comprehensive guide to the language and its uses
- [Python Module of the Week](http://pymotw.com/2/) - Learning the standard library by example
- [The docs themselves! 2.x for this class](https://www.python.org/doc/) - Learn what is and how to use the standard library

There are many, many good resources for learning the language of Python and how to do awesome things with it.
Those listed above are just a few based on personal experience and strong recommendations.

###  OS / Environment / Versions
[Digital Ocean $10 Credit](https://m.do.co/c/a4d54c9e5004) An easy way to get a free linux environment. If you are on windows, you can login with [PuTTY](http://www.putty.org/).

[Amazon's AWS has a free tier that allows you 750 compute hours every month of their t2.micro instances for 12 months](http://aws.amazon.com/free/)

- Use EC2 to create an instance from the Ubuntu 16.04 AMI for the most well known and supported platform

For the sake of our sanity we use Python 2 for this course.

Installing Python with [The Hitchhiker’s Guide to Python!](http://docs.python-guide.org/en/latest/)

Emergency Python Command Line: [http://repl.it/languages/Python](http://repl.it/languages/Python)

**We accept refugees using all operating systems. You will be politely prodded in the direction of solutions that are closer to [POSIX standards](http://en.wikipedia.org/wiki/POSIX#Mostly_POSIX-compliant)**

Some routes:
1. Install a linux virtual machine on another computer using virtualbox.
2. Use the command line in your apple machine.
3. Explore [POSIX for windows](http://en.wikipedia.org/wiki/POSIX#POSIX_for_Windows)

Another key tool is git:
* Windows: http://git-scm.com/download/win
* Mac: http://git-scm.com/download/mac
* Linux: (use your package manager)

### Mailing List
Sign up for the [Noisebridge Python Mailing List](https://www.noisebridge.net/mailman/listinfo/python) to hear updates and conversations regarding the course!

The mailing list uses GNU Mailman and pipermail.  To search archives you may find it helpful to download the archive `.tar.gz` (compressed) file and use regular expressions (`grep`) to search.

The Python Class Google Group Closed on Tuesday, November 3rd, 2015.
