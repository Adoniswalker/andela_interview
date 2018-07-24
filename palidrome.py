# Importing the library
from collections import deque

# Creating a Queue
queue = deque()


def palidrome_checker(word):
    global queue
    word = word.strip().lower()
    if len(queue) < 5:
        queue.append(word)
    else:
        queue.popleft()
        queue.append(word)
    return word == word[::-1]


names = ['Anna',
         'Civic',
         'Kayak',
         'Level',
         'Madam',
         'Mom',
         'jamo'
         'Noon',
         'Racecar', 'madam']

for word in names:
    print(palidrome_checker(word))
