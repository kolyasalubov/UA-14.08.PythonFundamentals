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
There should be one -- and preferably only one -- obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# ====== find the number of occurrences words: better, never, is. ======
words_to_count = ["better", "never", "is"]
word_counts = {word: 0 for word in words_to_count}
words = python_philosophy.split()

for word in words:
    if word in word_counts:
        word_counts[word] += 1

for word, count in word_counts.items():
    print(f"'{word}' occurs {count} times in the Python's phlosophy")

# ====== display text in uppercase ======
python_philosophy_uppercase = python_philosophy.upper()
print(python_philosophy_uppercase)

# ====== replace all occurrences "i" with "&" ======
modified_paragraph = python_philosophy.lower().replace("i", "&")
print(modified_paragraph)

