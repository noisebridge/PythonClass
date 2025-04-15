# Download the sample data from Hacker News API used in the lesson.

import csv

import requests

# resp = requests.get('https://hacker-news.firebaseio.com/v0/maxitem.json')
# id_max = resp.text
# id_int = int(id_max)

resp = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
ids = resp.json()

columns = [
    'id',
    'deleted',
    'by',
    'time',
    'text',
    'dead',
    'poll',
    'url',
    'score',
    'title',
    'descendants',
]

count = 0
with open('links.csv', 'a') as f:
  writer = csv.writer(f)
  # writer.writerow(columns)
  # for id_ in range(id_int - 8000, id_int - 12000, -10):
  for id_ in ids:
    resp = requests.get(
        f'https://hacker-news.firebaseio.com/v0/item/{id_}.json')
    item = resp.json()
    if item['type'] == 'story':
      count += 1
      print(id_, count)
      item_row = [item[c] if c in item else None for c in columns]
      writer.writerow(item_row)