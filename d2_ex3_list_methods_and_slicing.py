# FIFO pattern:
queue = []
queue.append("elem 1")
queue.append("elem 2")
queue.append("elem 3")
queue.pop(0)
queue.pop(0)
queue.pop(0)

# # echivalent...
# queue = []
# queue.insert(0, 'elem 1')
# queue.insert(0, 'elem 2')
# queue.insert(0, 'elem 3')
# queue
# queue.pop()
# queue.pop()
# queue.pop()


# LIFO pattern
stack = []
stack.append("elem 1")
stack.append("elem 2")
stack.append("elem 3")
stack.pop()
stack.pop()
stack.pop()

# # sau...
# # (cel mai nefericit dpdv re-indexare)
# q = []
# q.insert(0, "elem 1")
# q.insert(0, "elem 2")
# q.insert(0, "elem 3")
# q.pop(0)
# q.pop(0)
# q.pop(0)

from collections import deque

# deque este linked list
# operațiunile .append() .pop() .appendleft() .popleft()
# sunt eficiente (nu există re-indexare)
#
# dar accesul după index este ineficient!

# de asemenea, deque suportă o lungime maximă.
# aplicabilitate: sliding window + average

from random import randint

stream = [randint(0, 100) for _ in range(20)]
dq = deque([], 5)
for elem in stream:
    dq.append(elem)
    print("current average", sum(dq) / len(dq), '||', dq)


## slicing ##

# două puncte = sintaxă de slice;
# sintaxa completă de slice este start:stop:step

lst = ["ala", "bala", "porto", "cala"]

lst[1:3]

# toate elementele până la ultimul (exclusiv)
lst[0:-1]
lst[:-1]

# toate elementele
lst[:]
lst[None:None]

# primele 2 elemente:
lst[:2]

# în ordine inversă, step negativ
lst[3:1:-1]
lst[3:1:-2]
lst[::-2]
lst[::-1]

# în ordine inversă toate elementele,
# scriind manual indecșii:

# nu prinde tot
lst[-1:0:-1]

# nu merge
lst[-1:-1:-1]

# merge doar așa
lst[-1::-1]


## slicing funcționează la fel pe string-uri ##

s = "Bună după amiaza!"

# acestea sunt echivalente
lst[1:3]
lst[1:3:]
lst[1:3:1]

s[:5]
s[-5:]
