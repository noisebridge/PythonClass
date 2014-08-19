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
        if word in stop_words or support_words:
            clean_text.append(word) 
    return clean_text

#what code will look like without introducing concepts first
def func_clean_text(text, remove_words=(stop_words, support_words)):
    with open(text) as fp:
        full = fp.read()
    for i in (word for word in full.split() if word in stop_words or support_words):
        yield i

#brief overview of generators and comprehensions


imp_14 = imp_clean_text("obama_14.txt", remove_words=(stop_words, support_words))
func_14 = func_clean_text("obama_14.txt", remove_words=(stop_words, support_words))
print(len(imp_14))
print(len(list(func_14)))

#what will this give us knowing what we can remember about generators
print(imp_14 == list(func_14))

#how about this?
print(imp_14 == list(func_clean_text("obama_14.txt", remove_words=(stop_words, support_words))))






#heavier duty gen expressions, probably omit

from itertools import chain
def func_clean_text(text, remove_words=(stop_words, support_words)):
    with open(text) as fp:
        full = fp.read()
    for i in (word for word in full.split() if word not in chain(stop_words, support_words)):
        yield i




def gen_tokens(text):
    """ str -> gen 
    call nltk's work_tokenize function on our text,
    which differs from just splitting our list by spaces
    """
    for word in text.split():
        yield word

def gen_cleaner_words(text):
    """ str -> str 
    removes commonly 'attached' punctuation marks such as ',''.''*word*' etc.
    """
    for i in list(gen_tokens(text)):
        yield i.translate(None, "!@#$%^&*().,[]+=-_`~<>?")

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

#note for this module's purpose the default type for stop_words will be lowercase
def gen_ns_and_nsup_words(text):
    """ str -> gen 
    generate words not in stop or support words list 
    """
    for i in (word for word in gen_ns_words(text) if word.lower() not in support_words):
        yield i

#print(list(chain(stop_words, support_words)))


#test by print statement
f1 = func_clean_text("obama_14.txt")
#print(list(f1))
f2 = gen_ns_and_nsup_words("obama_14.txt")
#print(list(f2))

#print "up" in f1
