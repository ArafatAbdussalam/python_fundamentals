"""
methods of list objects:
append, insert, extend, remove, pop, extend, clear, index, count, sort, reverse, copy
"""

fruits =[ "kiwi", "blueberry", "pear", "pineapple", "pear", "melon", "muskmelon", "banana", "kiwi"]

print(fruits.count("kiwi"))
fruits.reverse()
print(fruits)
print(fruits.pop())

fruits.append("grape")
print(fruits)
print(fruits.sort())
fruits.index("pear")

stack = [3, 4, 5]
stack.pop()

print(stack)

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Garry")
queue.append("Graham")
print(queue)


queue.popleft( )
print(queue)
queue.popleft()

squares = list(map(lambda x: x**2, range(10)))

print(squares)

squares = [x**2 for x in range(10)]



combs = [ ]
for x in [1, 2, 3]:
	for y in [3, 1, 4]:
		if x != y:
			combs.append((x, y))
print(combs)

# this is concise and more readable

l = [(x, y) for x in [1, 2, 3] for y in (3, 1, 4) if x != y]
print(l)


print("*" * 50)

vec = [-4, -2, 0, 2, 4]
mbytwo = [x*2 for x in vec]
print(mbytwo)

positivenums = [x for x in vec if x>= 0]
print(positivenums)

# apply a function to all the elements

print([abs(x) for x in vec])

# call a method on each element
freshfruit = [ " banana", " loganberry", " passion fruit"]
c = [weapon.strip() for weapon in freshfruit]
print(c)

max =[ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in max for num in elem])

from math import pi
print([str(round(pi, i)) for i in range(1, 6)])

matrix = [
	[ 1, 2, 3, 4 ],
	[ 5, 6, 7, 8],
	[9, 10, 11, 12]
]

r = [[row[i] for row in matrix ] for i in range (4)]


del matrix[2:4]

print(r)

a = set("abracadaba!")
b = set("alacarazram")
print(a)
print(b)
print(a & b )
print(a - b)
print(a or b)
print(a | b)
print(a ^ b)

#set comprehension
a = { x for x in "abracadaba" if x not in "abc"}
print(a)

# waoh! this is sweeeet! I want more!
# You're doing pretty cool, Arafat. I love this

tel = {"Jack": 4098, "sape": 4139}
tel["guido"] = 4127
print(tel)
print(tel["Jack"])
del tel["sape"]

tel["irv"] = 4127

print(list(tel))
print(sorted(tel))
print("guido" in tel)
print("food" in tel)

dict(sape = 4139, jack = 4098)

x = {x: x**2 for x in (2, 4, 6)}
print(x)

knights = {"gallahad": "the pure", "robin": "the brave"}
for n, m in knights.items():
	print(n, m)

for i, v in enumerate(["tic", "tac", "toe"]):
	print(i,v)
	

questions = ["name", "quest", "favourite colour"]
answers = ["lancelot", "the holy grail", "lilac"]

for q, a in zip(questions, answers):
	print("what is your {}?  It is {}".format(q, a))
	
for i in reversed(range(1, 10, 2)):
	print(i)
	
basket = ["apple", "orange", "banana", "pear", "apple"]
for i in sorted(set(basket)):
	print(i)
	
	
import math

raw_data = [56.2, float("NaN"), 51.7, 55.3, 52.5, float("NaN"), 47.8]
filtered_data =[ ]
for value in raw_data:
	if not math.isnan(value):
		filtered_data.append(value)
print(filtered_data)

string1, string2, string3 = "", "Trondheim", "Hammer Dance"

non_null = string1 or string2 or string3
print(non_null)