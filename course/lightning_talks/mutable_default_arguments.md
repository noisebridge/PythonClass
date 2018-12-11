Mutation is forever
===================
Functions have parameters that you pass as you call them.

```python
def add(x, y):
    return x + y

add(1, 1)  # 2
```

You can make these optional, by providing default values

```python
def hello(who='Noisebridge'):
    return f'hello {who}!'

hello()  # 'hello noisebridge!'
```

Creating functions with mutable collections as the default leads to counter intuitive behavior

```python
def add_to_group(person, group=[]):
    group.append(person)
    return group

add_to_group('tom', ['jerry'])  # ['tom', 'jerry']
add_to_group('Haight', ['Ashberry'])  # ['Haight', 'Ashberry']
add_to_group('noisebridge')  # ['noisebridge']
add_to_group('noisebridge')  # ['noisebridge', 'noisebridge']


Why does this happen, and how can it be avoided?
