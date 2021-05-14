print("Standard Calculator")

def sum(a, b):
	print("sum -->", a+b)

def substract(a, b):
    print("substract -->", a-b)
    
def multiply(a, b):
    print("multiply -->", a*b)

def devide(a, b):
    print("devide -->", a/b)


def power(a, b):
    print(a**b)

# function call
no1 = 10
no2 = 2

sum(no1, no2)
substract(no1, no2)
multiply(no1, no2)
devide(no1, no2)


print("Advance Calculator")
power("power -->", no1, no2)
