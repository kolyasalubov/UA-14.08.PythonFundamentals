python_philosophy = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those! 
"""

better_count = 0
never_count = 0
is_count = 0

python_philosophy_split = python_philosophy.split()

for i in python_philosophy_split:
    if i == 'better':
        better_count += 1
    elif i == 'never':
        never_count += 1
    elif i == 'is':
        is_count += 1

print(f'better - {better_count}\n'
      f'never - {never_count}\n'
      f'is - {is_count}')

print('------------')
print(python_philosophy.upper())
print('------------')

python_philosophy_list = list(python_philosophy)

print(python_philosophy.replace('i', '&'))
