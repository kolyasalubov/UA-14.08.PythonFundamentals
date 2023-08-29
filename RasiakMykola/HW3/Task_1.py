
# 03.1 PRACTICAL TASKS / [GITHUB]


# Task1. 
the_zen_of_python = '''Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!'''

occurrences_better = the_zen_of_python.count('better')
occurrences_never = the_zen_of_python.count('never')
occurrences_is = the_zen_of_python.count('is')

text1 = the_zen_of_python.upper()

text2 = the_zen_of_python.replace('i','&')

print(f'\nNumber of occurrences of the word \'better\' = {occurrences_better}', \
      f'\nNumber of occurrences of the word \'never\' = {occurrences_never}', \
      f'\nNumber of occurrences of the word \'is\' = {occurrences_never}')
      
print(f"\n{text1}")
print(f"\n{text2}") 
     
