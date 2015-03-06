####Introduction to Pandas

update with install instructions:   
    
    pip install "ipython[notebook]"



    warm-up: dive right into pandas with .csv files in current directory, we'll address installations and foundations of pandas later   


DataTypes:  

Two primary data structures of pandas:  
-Series (1-dimensional)     
-DataFrame (2-dimensional)      

-Series is often called TimeSeries and though it is one-dimensional it still of course includes an index, which is usually a point in time   
-DataFrame is 2-dimensional and would include everything else that is feasible to handle in pandas      

One common mistake is to let yourself think that indexes are columns. They are not. Please do not treat them as if they are.    

Pandas does not implement significant modeling functionality outside of linear and panel regression     

Any corpus with more than just a few thousand rows of data should consider a different technology than pandas such as Spark. 

Optimized methods: .at, .iat, .loc, .iloc and .ix
-loc (label oriented, i is index)
can slice this way

Most important thing to remember: applying to domains with expertise

-what does pandas install?    
-[why numpy?](http://stackoverflow.com/questions/993984/why-numpy-instead-of-python-lists) pandas is built on top of numpy    
-basic type uniformity, you sacrifice for the flexibility of python lists    
-also the methods on the ndarray already weritten for you   
    x = numpy.fromfile(file=open("data"), dtype=float).reshape((100, 100, 100))         
-you do pay for speed with memory with ndarrays    
-numba and blaze are being developed, which are    
-supposedly both faster and more efficient but this is more used now    


Slightly More Advanced:     
-we'll leave apply and mapapply for next class after the lambda     
-vectorized mathematical and string ops, very easy      
-practicing ETL (Extract, Transform, Load) loops    

RESOURCES:   
-[Doc's themselves: they're great!](http://pandas.pydata.org/) 10-min guide, tuts, cookbook     
-[Great blog post on Top 10 Useful Pandas:](http://manishamde.github.io/blog/2013/03/07/pandas-and-python-top-10/) great quick reference and place to get up and running    
-[Neckbeard Republic:](http://neckbeardrepublic.com/tagged/pandas)Awesome Screencasts       
-[Wes's book: paid link](http://shop.oreilly.com/product/0636920023784.do)  only a small portion of it is outdated, but docs might be better    
-[Pandas cookbook youtube vids, low audio quality:](https://www.youtube.com/watch?v=eRpFC2CKvao&list=PLyBBc46Y6aAz54aOUgKXXyTcEmpMisAq3) more examples of thinking through problems     
-[Practical Business Python:](http://pbpython.com/) really awesome resource on just what the title says     
-[What's new in pandas talk:](https://www.youtube.com/watch?v=PUsntnCp65c) pydata nyc late '14. PyData posts most of their talks    

Going Further:      
-more of the sci-py stack, the web and SQL      
-[sklearn-pandas](https://github.com/paulgb/sklearn-pandas)    
-rpy2 also provides a way to convert R objects into Python objects      


From 10 things to hate about pandas:
Introducing codename 'badger'   
-1 not a database bc its too far from metal, but there are tricks and libs to use it with dbs   
-2 no support for memory maps   
-3 no tight db integration, ODBC C API may come later   
-4 N/A needs a bit of work and to be first class citizen    
-5 RAM management   
-6 weak support for categorical data    
-7 complex GroupBy slower and messier than they could be, custom funcs for .apply()     
-8 appending data slow and tedious  
-9 limited type system column metadata  
-10 no true query processing layer  
-11 slow no multicore distributed algos     

note: this might be a paid system, and since the time of this announcement Wes's company was acquired 


    import pandas as pd     
    import numpy as np  
    import matplotlib.pyplot as plt     
    pd.options.display.mpl_style = 'default'    
    %matplotlib inline      


Resources:  
[Greg Reda's tut](http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/) listed in official docs   
[Practical Business Python](http://pbpython.com/simple-graphing-pandas.html) simple graphing, but there's lots more on this site      