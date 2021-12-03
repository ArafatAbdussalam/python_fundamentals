pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]

pairs.sort(key=lambda pair: pair[1])
print(pairs)

def fib(n):
	""" print a Fibonacci series up to n """
	a, b = 0, 1
	while a < n:
		print(a, end= ' ')
		a, b = b, a + b
	print()
	
fib(2000)

f = fib
f(100)
f(0)


def fib2(n):
	""" Return a list containing the Finonacci series up to n """
	result = [ ]
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
		return result
		
	f100 = fib2(100)
	f100
	
	
def ask_ok(prompt, retries=4, reminder="Please, try again!"):
	while True:
		ok = input(prompt)
		if ok in ("y", "ye", "yes"):
			return True
		if ok in("n", "no", "nop", "nope"):
			return False
		retries -= 1
		if retries < 0:
			raise ValueError("invalid user response")
			print(reminder)
			
			
ask_ok("Do you really want to quit?")
ask_ok("Ok to overwrite the file?", 2)
ask_ok("OK to overwrite the file?", 2, "Com'on, only yes or no")

# "in" tests whether or not a sequence contains a certain value

i = 5

def f(arg=i):
	print(arg)
	
i = 6
f()


def b(a, L = [ ]):
	L.append(a)
	return L

print(b(1))
print(b(2))
print(b(3))
print(b(4))

def c(a, L = None):
	if L is None:
		L = [ ]
	L.append(a)
	return L
	
# keyword aeguments
	
def parrot(voltage, state = "a stiff", action = "Voom", type = "Norwegian Blue"):
	print("-- This parrot wouldn't", action, end=" ")
	print("if you put", voltage, "volts through it")
	print("-- Lovely plumage, the", type)
	print("it's", state, "!")


# parrot(1, 2, 3)
# Hmmm! I see what this does

parrot(1000)
# print(voltage=1000)

def cheeseshop(kind, *arguments, **keywords):
	print("-- Do you have any", kind, "?")
	print("-- I'm sorry we're all out of", kind)
	for arg in arguments:
		print(arg)
	print("-" * 50)
	for kw in keywords:
		print(kw, ":", keywords[kw])
		
cheeseshop("Limburger", "It's very runny, sir.",
"It's really very, VERY runny, sir.",
shopkeeper="Michael Palin",
client="John Cleese",
sketch="Cheese Shop Sketch")

