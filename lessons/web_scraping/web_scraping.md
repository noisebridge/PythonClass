####Web Scraping with Scrapy

installation: requires third-party module scrapy    

    spike: look at an example of an html page in the web console,    then figure out how to select certain elements of the DOM using XPath in the console    

Developer Tools gives you the ability to test XPath selectors in the JavaScript Console by using $x – eg: $x("//img")

What is XPath? and [xpath selectors](http://www.w3schools.com/XPath/xpath_syntax.asp) yes, this is w3schools but even MDN links here!
'[XML Path Language](https://developer.mozilla.org/en-US/docs/Web/XPath), powerful way of navigating through the DOM of any XML based language documents, such as HTML and XUL' 

note: watch out how you craft your Xpath queries, there can be lots of tricky spaces and such within the html and tags  

1. Script Integration: let’s see how to get just the information we want back into our core language, python, using our core language, python.  
-go to virtualenv and then get ready to start your scrapy project through a CLI script much like in django  
-briefly examine what we have installed and setup   
-before we actually think about sending out the robots let’s make sure that we know the terms of use and what it says in the robots.txt     
-what page do we want to crawl and how can we navigate to the best results possible if applicable      
-eg: we want the top python questions: so we type in python to the search on SO and then sort by votes, because the site offers that to us for free
got to check out the domains sorting options as well
'http://stackoverflow.com/questions?pagesize=50&sort=newest'    

2. Writing Spider within framework  
-write the most basic spider for the site that we have already chosen   
-[refer to the docs to find out what these Items and Fields are](http://doc.scrapy.org/en/latest/topics/items.html)     
-Items are containers for the data  
-Fields are metadata in the form of attributes, but are just ‘plain-old’ Python dicts.  
-after assigning a Field we use Item.fields and use the Item object like a typical python dict API      

    command to make it into json:   
    scrapy crawl <spidername> -o items.json -t json   OR    
    scrapy crawl <spidername> -o items.csv -t csv   

3. Underlying code: take a step back 
-what's happening when you write the command    
    scrapy crawl <spidername>   
-what the parse function actually does  
-[knowing how the spiders work](http://doc.scrapy.org/en/latest/topics/spiders.html)
-how scrapy is async?    
-diff between base spider and crawl spider     

4. Pick a new website together and repeat that basic process       


additional:     
[Is scrapy worth your time?](http://stackoverflow.com/questions/6283271/is-it-worth-learning-scrapy) 

Also, scrapy is the most robust in that you can customize is the most if the data you are scraping becomes complicated  

other python scraping libraries: BeautifulSoup, Mechanize, requests, lxml
'Beautiful Soup sits on top of popular Python parsers like lxml and html5lib'
scrapy cloud    

[what’s wrong with using regex for html:](http://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags?page=1&tab=votes#1732454)
regular expressions are for parsing regular languages, html is not a regular language, from there we go into applied automata theory    

web pages are designed as APIs between the html tags and the designers who make and change the css methodically     

there can be bugs in data extraction and data saving such as unicode or ascii bugs   




resources:  
[realpython.com - scrapy with mongodb pipeline](https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/)

