The Noisebridge Python Class meets every Monday from 7 to 9 PM (PT) in the 2nd
floor Electronics Room at Noisebridge in San Francisco.

The course is free! If you wish to donate, please give to
[Noisebridge](https://donate.noisebridge.net).

- Recommended donations: $15, $50, $200+
- Recommended monthly donations: $10, $20, $40, $80+ / month

All Python classes follow the [Noisebridge Anti-Harrasment
Policy](https://www.noisebridge.net/wiki/Anti-Harassment_Policy), the
[Noisebridge Conflict Resolution
Guide](https://www.noisebridge.net/wiki/Conflict_Resolution) and the recurse.org
[Social Rules](https://www.recurse.com/social-rules)

After class, we welcome your feedback! Submit the form
[here](https://forms.gle/423wBNBgzRHt5o4h6)

Contents:

- [Curriculum](#sample-curriculum)
- [Course Description](#class-description-goals-and-ideal-student)
- [New Student Reading](#new-student-reading)

### Sample Curriculum

The Noisebridge Python Class has existed at least as far back as 2015, with many
different instructors and incarnations as far as I can tell.

As of May 2023, the class is being redesigned/rebooted and a new curriculum is
being designed. Travis B (audiodude/tmoney) is attempting to do this largely by
himself, so be patient!\
The following are links to samples of the old curriculum but may not be
completely representative of what will be taught in the new course.

The old course was 6 weeks of lectures, followed by 4 guest lectures and a week
off. We're still determining the best way to teach the new course, but it might
be in the form of Lecture A being taught for two weeks, followed by Lecture B
for two weeks. So six lectures over the course of 12 weeks (more leeway to miss
a week).

- [JSON and File Handling](archive/course/file-handling-and-json)
- [String Methods and Usage](archive/course/strings)
- [The Sqlite3 Database Library](archive/course/sqlite3)
- [Writing an Algorithm](archive/course/algorithms)
- [Functional Programming in Python](archive/course/higher-order-functions)
- [Intro to Microservices with Flask](archive/course/flask)

### Course Description, Goals, and Ideal Student

The course is designed with the following constraints in mind:

- The barrier to entry is low, but the pace is fast.
- All materials must be made [available on
  Github](https://github.com/audiodude/PyClass).
- Each lesson stands alone, so it's okay to miss a week!
- The core, repeated modules are regularly updated.

To best experience the course, spend a short time reviewing the materials
beforehand. If you wish to know what's scheduled for this week, please join [the
mailing list](#mailing-list) and send an email out to PyClass@googlegroups.com

#### Prerequisites

Ideally, students starting the course can grasp the following code. Feel free to
use web resources to look up anything you don't understand!

```python
letter_frequency_dict = {}
word = "noisebridge"

for letter in word:
    times = letter_frequency_dict.get(letter, 0)
    times += 1
    letter_frequency_dict[letter] = times
```

#### We use the [Socratic Method](http://www.criticalthinking.org/pages/socratic-teaching/606)

A Socratic questioner should:

1. Keep the discussion focused
2. Keep the discussion fact-based\*
3. Stimulate the discussion with probing questions
4. Periodically summarize what has and what has not been dealt with and/or
   resolved
5. Draw as many students as possible into the discussion.

\* [intellectually
responsible](https://en.wikipedia.org/wiki/Intellectual_responsibility) can be
effectively replaced with 'fact-based' for our needs.

### New Student Reading

#### Installing Python

No Python installation necessary!

For this course, we use a shared Python [Jupyter Hub](https://jupyter.org/hub)
service. To create an account on the service, simply visit the
[homepage](http://sfpythonlab.com/) and type your desired username in the
username box and the shared global password in the password box. **The password
will be shared during class sessions**.

You can also click the links for individual lesson notebooks, which will open in
the shared Jupyter Hub environment and prompt you to login or create an account.

Please do not attempt to access other students accounts or otherwise hack this
shared resource!

With all that said, if you would like help with installing a Python environment
on your personal computer, reach out to one of the instructors. We use Python 3
exclusively, as Python 2 is EOL (end of life).

#### Python Resources

If you are new to Python or to programming in general, here are some excellent
resources:

- [The Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [Learn Python the Hard Way](http://learnpythonthehardway.org/)
- [Byte of Python](http://www.swaroopch.com/notes/python/)
- [Learning Python, 5th
  edition](http://shop.oreilly.com/product/0636920028154.do) (Also available at
  the SF public library!)

Once you feel comfortable with the basics of the language, you can explore the
standard library!

- [The Official Python Library
  Documentation](https://docs.python.org/3/library/)
- [Python Module of the Week](http://pymotw.com/3/)

There are many, many good resources for learning the language of Python and how
to do awesome things with it. Those listed above are just a few based on
personal experience and strong recommendations.

### OS / Environment / Versions

As mentioned above, the course is taught from a shared Jupyter Hub instance. No
installation is necessary and it should work on any computer that has a web
browser.

## Connecting

Feel free to connect with us on the `#python` channel in [Noisebridge
Discord](https://www.noisebridge.net/wiki/Discord)!
