with open("reddit_fav_about_python.txt") as fp:
    full = fp.read()


just_words = full.split()

sw = [' ', " '", '!', '"', '#', '&', "'", "'re", "'s", '(', ')', '*', '+', ',', '-', '--', '.', '...', '/', ':', ';', '?', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '``', 'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'amp', 'an', 'and', 'any', 'are', 'as', 'at', 'b', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'c', 'can', 'd', 'did', 'do', 'does', 'doing', 'don', 'down', 'during', 'e', 'each', 'f', 'few', 'for', 'from', 'further', 'g', 'h', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'itself', 'j', 'just', 'k', 'l', 'm', 'me', 'more', 'most', 'must', 'my', 'myself', 'n', "n't", 'no', 'nor', 'not', 'now', 'o', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'p', 'q', 'r', 'raquo', 's', 'same', 'she', 'should', 'so', 'some', 'such', 't', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'u', 'under', 'until', 'up', 'v', 'very', 'w', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'x', 'y', 'you', 'your', 'yours', 'yourself', 'yourselves', 'z', '|']
support_words = ['about', 'above', 'after', 'again', 'against', 'all', 'am', 'amp', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'did', 'do', 'does', 'doing', 'don', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'if', 'in', 'into', 'is', 'it', 'its', 'itself', 'just', 'me', 'more', 'most', 'must', 'my', 'myself', "n't", 'no', 'nor', 'not', 'now', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'raquo', 'same', 'she', 'should', 'so', 'some', 'such', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'you', 'your', 'yours', 'yourself', 'yourselves']

def imp_clean_text(text, stop_words=[]):
    with open(text) as fp:
        full = fp.read()
    clean_text = list()
    for word in full.split():
        if word in stop_words or support_words:
            clean_text.append(word) 
    return clean_text

imp = imp_clean_text("reddit_fav_about_python.txt", stop_words=[sw, support_words])


sw = [' ', " '", '!', '"', '#', '&', "'", "'re", "'s", '(', ')', '*', '+', ',', '-', '--', '.', '...', '/', ':', ';', '?', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '``', 'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'amp', 'an', 'and', 'any', 'are', 'as', 'at', 'b', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'c', 'can', 'd', 'did', 'do', 'does', 'doing', 'don', 'down', 'during', 'e', 'each', 'f', 'few', 'for', 'from', 'further', 'g', 'h', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'itself', 'j', 'just', 'k', 'l', 'm', 'me', 'more', 'most', 'must', 'my', 'myself', 'n', "n't", 'no', 'nor', 'not', 'now', 'o', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'p', 'q', 'r', 'raquo', 's', 'same', 'she', 'should', 'so', 'some', 'such', 't', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'u', 'under', 'until', 'up', 'v', 'very', 'w', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'x', 'y', 'you', 'your', 'yours', 'yourself', 'yourselves', 'z', '|']
support_words = ['about', 'above', 'after', 'again', 'against', 'all', 'am', 'amp', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'did', 'do', 'does', 'doing', 'don', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'if', 'in', 'into', 'is', 'it', 'its', 'itself', 'just', 'me', 'more', 'most', 'must', 'my', 'myself', "n't", 'no', 'nor', 'not', 'now', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'raquo', 'same', 'she', 'should', 'so', 'some', 'such', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'you', 'your', 'yours', 'yourself', 'yourselves']

def get_clean_word_ls(text, stop_words=[sw, support_words]):
    with open(text) as fp:
        full = fp.read()
    return [word for word in full.split() if word not in sw or support_words]

def get_sortedls_of_wordlengths(text):
    return sorted([len(w) for w in get_clean_word_ls(text)])


func = func_clean_text("reddit_fav_about_python.txt", stop_words=[sw, support_words])

#clean just using regex
import re
def diff_clean_text(text):
    with open(text) as fp:
        full = fp.read()
    return re.sub('^[^a-zA-z]*|[^a-zA-Z]*$','', full)



#just_words = (word for word in full)
print(just_words)

def all_words(text):
    with open(text) as fp:
        all_lines = list()
        for line in fp:
            all_lines.append(line)
    return all_lines

#print(all_words("reddit_fav_about_python.txt"))

#now = str(all_words("reddit_fav_about_python.txt").splitlines().rstrip()


