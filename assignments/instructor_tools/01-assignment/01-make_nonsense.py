import string
import random

WORD_LENGTH = 4
REPEAT_NUM = 5
TOTAL = 20

words = []
for _ in range(REPEAT_NUM):
  words.append(''.join(random.choices(string.ascii_lowercase, k=WORD_LENGTH)))
words += [''.join(random.sample(word, len(word))) for word in words]

for _ in range(TOTAL - (REPEAT_NUM * 2)):
  words.append(''.join(random.choices(string.ascii_lowercase, k=WORD_LENGTH)))

random.shuffle(words)

with open('nonsense2.txt', 'w') as f:
  f.write('\n'.join(words) + '\n')