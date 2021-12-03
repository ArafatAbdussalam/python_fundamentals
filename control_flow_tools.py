x = int(input("Please enter an integer:  "))

if x < 0:
	x = 0
	print("Negative changed to zero ")
	
elif x == 0:
	print("Zero")

elif x == 1:
	print("Single")
else:
	print("More")
	

words = ["cat", "Windows", "defenestration"]

for w in words:
	print(w, len(w))
	

users = {"Hans": "active", "Èlènore": "inactive", "Yun": "active"}

# iterate over a copy
for user, status in users.copy().items():
	if status == "inactive":
		del users[user]
		
active_users = {}

# create a new collection
for user, status in users.items():
	if status == "active":
		active_users[user] = status
		
for i in range(5):
	print(i)
	
print(list(range(4,15)))

print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))


a = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(a)):
	print(i, a[i])

for n in range(2, 10):
	for i in range(2, n):
		if n % x == 0:
			print(n, "equals", x, "*", n/x)
			# break or continue
			break
		else:
			print(n, "is a prime number")
			
# the pass statement is used when a statement is required syntatically but the program requires no action. it's also used as a placeholder for a function.

"""
def http_error(status):
			match status:
				case 400:
					return "Bad request"
				case 404:
					return "Not found"
				case 418:
					return "I am a teapot"
				case _:
					return "Something is wrong with the internet"
					

case 401 | 403 | 404:
			return "Not Allowed"


# point is an x, y tuple

match point:
	case (0, 0):
		print("Origin")
	case (0, y):
		print(f"Y = {y}")
	case _:
		raise ValueError("Not a point")
	


class Point:
	x: int
	y: int

def where_is(point):
	match point:
		case Point (x = 0, y = 0):
			print(Origin)
		case Point ( x = 0, y = y):
			print(f"Y = {y}")
			#...
		case Point ():
			print("somewhere else")
		case _:
			print("Not a point")
			
"""
