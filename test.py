variable = ""
varname = 2
varstring = "jay"
print(varstring + str(varname))


age = 37
if age < 30:
    print("you're young")
elif age > 30:
    print("no worries, you're still young")
else:
    print("i don't know how you got here")


#lists
colors = ["red", "green", "blue"]
print(colors)
colors.append("yellow")
print(colors)
colors.remove("red")
print(colors)
print(colors[1])

for x in colors:
    print(x)

#dictionaries
me = {
    "first name": "john",
    "last name": "doe",
    "age": 21,
}
print(me)
#get a value
print(me["first name"])
me["age"]= 99
me["favorite color"]="blue"
print(me)

#function
def say_hello():
    print("hello")

def say_goodbye(name, age):
    print("goodbye "+name + " " + str(age))

#call functions
say_hello()
say_goodbye("john doe", 32)

#functions
def print_menu():
    print("1)add")
    print("2)subtract")
    print("3)multiply")
    print("4)divide")
    
#instructions
print_menu()
opt = int(input("choose an option: "))
num1 = float(input("please provide me the first number:"))
num2 = float(input("please provide me the second number:"))

if opt == 1:
    total = num1 + num2
    print("the total of those numbers is "+str(total))
elif opt == 2:
    total = num1 - num2
    print("the total of those numbers is "+str(total))
elif opt == 3:
    total = num1 * num2
    print("the total of those numbers is "+str(total))
elif opt == 4:
    if num1 == 0:
        print("you cannot divide by zero")
    elif num2 == 0:
        print("you cannot divide by zero")
    else:
        total = num1 / num2
        print("the total of those numbers is "+str(total))
#create the rest of the logic