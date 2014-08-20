#direct from iPython Notebook

#1 If you’ve done excel then you have done functional programming
#  Port excel work into python script

line1 = range(1, 9)
line2 = range(10, 50, 5)
#print test to see what we have correlates to excel data
print(line1, line2)

total = sum(line1) + sum(line2)

#have states changed?
print(line1, line2)

#or
print(sum(range(1,9)) + sum(range(10,50,5)))

#have states changed?
print(line1, line2)

#or 
from itertools import chain
print(sum(chain(range(1,9), range(10,50,5))))

#have states changed?
print(line1, line2)
 
#2 discussion of pros and cons of the above code and keep these principles in mind for the folowing


#3 brief overview of generators and comprehensions
#  intro to iterators terminology, list comps, and generators
iterable = range(20)
#i is the iterator
for i in iterable:
    print(i*2)

alpha_iter = "abcdefghijksmellonop"
for i in alpha_iter:
    print(i*2)

#but if we want it in a data structure that we can manipulate further
def get_double_letters(ltrs):
    doubles = list()
    for i in alpha_iter:
        doubles.append(i*2)
    return doubles

#list comprehensions
double_letters = [ltr*2 for ltr in alpha_iter]

#generator function
def gen_double_letters(ltrs):
    for i in alpha_iter:
        yield i*2    
 
#won't work btw
#for i in alpha_iter:
#    yield i*2        

print(get_double_letters(alpha_iter))
print(gen_double_letters(alpha_iter))

gen_object = gen_double_letters(alpha_iter)

gen_object.next()
gen_object.next()

list(gen_object)

#gen expressions! write them backwards at first
def gen_dubs(ltrs):
    for i in (ltr*2 for ltr in ltrs):
        yield i

#4 basic appiclation: compare cleaning text methods on larger text corpuses converted into iterables for processing
#let's apply this to our sample text 

#just test that we are in proper directory with proper files
with open("obama_09.txt") as fp:
    o_09 = fp.read()
with open("obama_14.txt") as fp:
    o_14 = fp.read()

#taken from augemented nltk list and experience
stop_words = [' ', " '", '!', '"', '#', '&', "'", "'re", "'s", '(', ')', '*', '+', ',', '-', '--', '.', '...', '/', ':', ';', '?', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '``', 'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'amp', 'an', 'and', 'any', 'are', 'as', 'at', 'b', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'c', 'can', 'd', 'did', 'do', 'does', 'doing', 'don', 'down', 'during', 'e', 'each', 'f', 'few', 'for', 'from', 'further', 'g', 'h', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'itself', 'j', 'just', 'k', 'l', 'm', 'me', 'more', 'most', 'must', 'my', 'myself', 'n', "n't", 'no', 'nor', 'not', 'now', 'o', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'p', 'q', 'r', 'raquo', 's', 'same', 'she', 'should', 'so', 'some', 'such', 't', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'u', 'under', 'until', 'up', 'v', 'very', 'w', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'x', 'y', 'you', 'your', 'yours', 'yourself', 'yourselves', 'z', '|']
support_words = ['about', 'above', 'after', 'again', 'against', 'all', 'am', 'amp', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'did', 'do', 'does', 'doing', 'don', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'if', 'in', 'into', 'is', 'it', 'its', 'itself', 'just', 'me', 'more', 'most', 'must', 'my', 'myself', "n't", 'no', 'nor', 'not', 'now', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'raquo', 'same', 'she', 'should', 'so', 'some', 'such', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'you', 'your', 'yours', 'yourself', 'yourselves']


def imp_clean_text(text, remove_words=(stop_words, support_words)):
    with open(text) as fp:
        full_text = fp.read()
    full_text_ls = full_text.split()
    clean_text = list()
    for word in full_text_ls:
        if word not in stop_words and support_words:
            clean_text.append(word) 
    return clean_text

#what code will look like without introducing concepts first
def func_clean_text(text, remove_words=(stop_words, support_words)):
    with open(text) as fp:
        full = fp.read()
    for i in (word for word in full.split() if word not in stop_words and support_words):
        yield i

imp_14 = imp_clean_text("obama_14.txt", remove_words=(stop_words, support_words))
func_14 = func_clean_text("obama_14.txt", remove_words=(stop_words, support_words))
print(len(imp_14))
print(len(list(func_14)))

#what will this give us knowing what we can remember about generators
print(imp_14 == list(func_14))

#how about this?
print(imp_14 == list(func_clean_text("obama_14.txt", remove_words=(stop_words, support_words))))


# %timeit magic magic method is only for ipython users
#%timeit imp_clean_text("obama_09.txt")
#%timeit func_clean_text("obama_09.txt")

#use time.timeit method in python interpreter
#from time import timeit
#imp09_timed = timeit("imp_09", setup=None, number=100000)
#imp14_timed = timeit("imp_14", setup=None, number=100000)

        
        

#5 deeper dive application: cleaning and manipulating raw text data into consummable information for end user
#quick itertools intro and begin text processing

#everything in itertools yields a generator!

from itertools import chain
def func_clean_text(text, remove_words=(stop_words, support_words)):
    with open(text) as fp:
        full = fp.read()
    for i in (word for word in full.split() if word not in chain(stop_words, support_words)):
        yield i


#heavier duty gen expressions

def gen_tokens(text):
    """ str -> gen 
    call split on our text when its a string
    """
    with open(text) as fp:
        fp = fp.read()
        for word in fp.split():
            yield word

def gen_cleaner_words(text):
    """ str -> str 
    removes commonly 'attached' punctuation marks such as ',''.''*word*' etc.
    note that this function does not remove any words from iterable
    """
    for i in gen_tokens(text):
        yield i.translate(None, "!@#$%^&*().,[]+=-_`~<>?:;")

def gen_lowercase_tokens(text):
    """ str -> gen 
    maintain generator type for lowercase words, 
    useful for quick comparisons against certain stop word lists
    """
    for word in gen_tokens(text):
        yield word.lower()

def gen_ns_words(text):
    """ str -> gen 
    need non stop words before non support words
    """
    for i in (word for word in gen_cleaner_words(text) if word.lower() not in stop_words):
        yield i

def gen_nsup_words_only(text):
    """str -> gen
    generate words not in support words, mostly a utility function
    """
    for i in (word for word in gen_tokens(text) if word.lower() not in support_words):
        yield i
        
#note for this module's purpose the default type for stop_words will be lowercase
def gen_ns_and_nsup_words(text):
    """ str -> gen 
    generate words not in stop or support words list 
    """
    for i in (word for word in gen_ns_words(text) if word.lower() not in support_words):
        yield i

#Analysis functions
def get_text_len_and_content_len(text):
    """ str -> float, float
    return length of text list with stop_words omitted and length of 'content'
    defined as non 'support words' """ 
    num_ns_tokens = float(len(list(gen_ns_words(text))))
    num_content_tokens = float(len(list(gen_ns_and_nsup_words(text))))
    return (num_ns_tokens, num_content_tokens)

def get_content_percentage(text):
    """ str -> float
    number of words in text - stop words and support words / number of tokens in text. 
    Note the difference between this ratio and the lexical diversity ratio, 
    which only accounts for unique words.
    """  
    try: 
        result = float(len(list(gen_ns_and_nsup_words(text)))) / float(len(list(gen_tokens(text))))
        result = round(result, 2)
    except ZeroDivisionError:
        pass
        result = 0
    finally:
        return result

#print(list(chain(stop_words, support_words)))


#test by print statement
f1 = func_clean_text("obama_14.txt")
#print(list(f1))
f2 = gen_ns_and_nsup_words("obama_14.txt")
#print(list(f2))

#print "up" in f1

get_content_percentage("obama_09.txt")
get_text_len_and_content_len("obama_09.txt")
print len(list(gen_cleaner_words("obama_09.txt")))

def gen_nsup_words_only(text):
    """str -> gen
    generate words not in support words, mostly a utility function
    """
    for i in (word for word in gen_tokens(text) if word.lower() not in support_words):
        yield i

gen_nsup_words_only("obama_09.txt")

len(list(gen_ns_words("obama_09.txt")))
len(list(gen_ns_and_nsup_words("obama_09.txt"))) 

get_text_len_and_content_len("obama_09.txt")

#quick detour into the collections module
from collections import Counter
ctr_obama_09 = Counter(gen_ns_and_nsup_words("obama_09.txt"))
ctr_obama_14 = Counter(gen_ns_and_nsup_words("obama_14.txt"))

#print(ctr_obama_09)
#for ipython users (otherwise use inspect module)
#ctr_obama_09?

#now for a bit more comparative analysis with a basic data type
set_obama_09 = set(gen_ns_and_nsup_words("obama_09.txt"))
set_obama_14 = set(gen_ns_and_nsup_words("obama_14.txt"))

#what can we do?
print len(list(gen_tokens("obama_09.txt")))
print len(set_obama_09)

print len(list(gen_tokens("obama_14.txt")))
print len(set_obama_14)

#NLP metric a la George Lakoff
def get_rough_keyword_ratio(text):
    return float(len(set(gen_ns_and_nsup_words(text)))) / float(len(list(gen_tokens(text)))) * 100

get_rough_keyword_ratio("obama_09.txt")
get_rough_keyword_ratio("obama_14.txt")


#6 fun with itertools

#a little fun with itertools
from itertools import *
#ifilter(len() > 10, gen_ns_and_nsup_words("obama_09.txt")) 
#is this helpful or gratuitous 

#ctr_obama_09[:10]  Type Error

for i in islice(ctr_obama_09, 10):
    print(i)

#frozenset(ctr_obama_09)

#funny pairs a la Louis Van Ahn's captcha?
#print(list(izip(set_obama_09, set_obama_14)))

#well its hard to apply these principles to text, most are meant for numbers
#see http://pymotw.com/2/itertools/

