from pandas import DataFrame, Series, read_csv
import pandas as pd #pandas import convention
import sys #only needed to determine Python version number

#just in case
print 'Python version ' + sys.version
print 'Pandas version ' + pd.__version__

df1 = DataFrame({'int_col' : [1,2,6,8,-1], 'float_col' : [0.1, 0.2,0.2,10.1,None], 'str_col' : ['a','b',None,'c','a'], 'groc_col' : ['apples','bananas','coconuts','dogfood',None],'rev_col':range(4,-1,-1)})
df2 = DataFrame({'first_col' : [13,12,-6,-8,-11], 'second_col' : [10.1, 10.2,10.2,110.1,None], 'str_col' : ['a','b',None,'c','X'], 'groc_col' : [None,'bananas','coconuts','dogfood',None],'rev_col':range(4,-1,-1)})

#stats
df1.describe() #only shows numbers

#gh.ix[:,['float_col', 'int_col']] less elegant
df1[['float_col', 'int_col']]

df1.fillna(value="waiting")

df1['div_col'] = df1['float_col'] / df1['int_col'] 

mean = df1['rev_col'].mean()
df1['mean_col'] = mean

new = pd.merge(df1,df2, how='outer', on='str_col')


#quick plotting
import numpy as np
plot_df = DataFrame(np.random.randn(1000,2),columns=['x','y'])

plot_df.hist()
plot_df.plot()


#series object 1-dimensional
days = ['mon', 'tues', 'weds', 'thurs', 'fri', 'sat', 'sun']
ratings = ['meh', 'erg', 'ugh', 'ok', 'alright', 'yauh', "d'oh"]

s1 = Series(days, ratings, name="what days are")
#cool to make data with date_range
s2 = pd.Series([1,2,3,4,5,6],index=pd.date_range('20130102',periods=6))