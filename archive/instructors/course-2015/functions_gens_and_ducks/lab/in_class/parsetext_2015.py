
import codecs

from collections import Counter

sw = [' ', " '", '!', '"', '#', '&', "'", "'re", "'s", '(', ')', '*', '+', ',', '-', '--', '.', '...', '/', ':', ';', '?', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '``', 'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'amp', 'an', 'and', 'any', 'are', 'as', 'at', 'b', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'c', 'can', 'd', 'did', 'do', 'does', 'doing', 'don', 'down', 'during', 'e', 'each', 'f', 'few', 'for', 'from', 'further', 'g', 'h', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'itself', 'j', 'just', 'k', 'l', 'm', 'me', 'more', 'most', 'must', 'my', 'myself', 'n', "n't", 'no', 'nor', 'not', 'now', 'o', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'p', 'q', 'r', 'raquo', 's', 'same', 'she', 'should', 'so', 'some', 'such', 't', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'u', 'under', 'until', 'up', 'v', 'very', 'w', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'x', 'y', 'you', 'your', 'yours', 'yourself', 'yourselves', 'z', '|']
support_words = ['about', 'above', 'after', 'again', 'against', 'all', 'am', 'amp', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'did', 'do', 'does', 'doing', 'don', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'if', 'in', 'into', 'is', 'it', 'its', 'itself', 'just', 'me', 'more', 'most', 'must', 'my', 'myself', "n't", 'no', 'nor', 'not', 'now', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'raquo', 'same', 'she', 'should', 'so', 'some', 'such', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'you', 'your', 'yours', 'yourself', 'yourselves']

with codecs.open('../pres_on_trade_2015.txt', encoding='utf-8') as fp:
    all_text = fp.read() 

all_words = all_text.split()

non_stop_words = (word for word in all_words if word.lower() not in sw)

non_support_words = (word for word in all_words if word.lower() not in support_words)

#clean_words = ( word[:-1] for word in non_support_words if word[-1] in ("'",".",":", ",", "?", "!") )

def gen_clean_words(word_sequence):
    for word in ( word[:-1] for word in word_sequence if word[-1] in ("'",".",":", ",", "?", "!") ):
        try:
            yield word 
        except UnicodeEncodeError:
            pass 

for word in gen_clean_words(non_support_words):
    print word 

avg_word_length = len(list(gen_clean_words(non_support_words))) / sum( [len(word) for word in list(gen_clean_words(non_support_words)) if len(word) != 0] )

#print avg_word_length


#word_freq = Counter(clean_words)




