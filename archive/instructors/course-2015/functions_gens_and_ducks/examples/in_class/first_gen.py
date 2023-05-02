with open('pres_on_trade_2015.txt', 'r') as fp:
    all_text = fp.readlines()
  

def gen_each_line(text):
    for line in text:
        yield line

all_lines = gen_each_line(all_text)  

print list(all_lines) 

