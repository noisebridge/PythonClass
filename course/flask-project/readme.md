Emulating ["Hacker News"](https://news.ycombinator.com/) using python's [flask web framework](http://flask.pocoo.org/)


####Getting Running
0. make sure to have cloned the [PyClass repo](https://github.com/PyClass/PyClassLessons)
1. create and activate a virtualenv this project uses python 2.7.X     
3. navigate to the flask-project directory    
    `$ pip install -r requirements.txt`    
4. open a python shell and give the command to initialize and create the sqlite db:     
```python    
>>> from models import createdb    
>>> create_db()    
```    
5. information on subsequent db migrations can be found with [flask-migrate docs](https://flask-migrate.readthedocs.org/en/latest/)    


####Goals    
0. upvotes    
    -with simple ajax call     
    -Please replace grayarrow.gif with Unicode character ▲ to make the upvote triangle look crisp on high-resolution displays    
1. comments    
    -updating models    
    -enabling replies    
    -updating front end in accordance with reply style    
2. auth and login    
    -reg form    
    -give logged in Users permissions/abilities to submit, vote, comment    
3. post link or text option    
    -cut down our urls into domains for viewing in template    
4. ranking algorithm    
 4a. cron job to save points and update ranking order    
5. basic html and css    
6. get it on remote server    
6. archives exposed and pagination    
7. basic outward facing web API    
8. newest section    
9. add "days ago" field    
10. add a FAVICON!! 

how do HN comments work? front and back-end



CRUD

Create: enter data into the database, through user entry or otherwise     
Read: query the database and display in html templates     
Update: query, modify, then save data back to the database     for this project: applies mostly to comments section    
Delete: delete records if necessary   for this project: is there delete?     