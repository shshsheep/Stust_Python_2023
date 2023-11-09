#exe_1

def i_nput(name,age) :
    print(name,age)

i_nput("james",20)

print("----------")
#exe_2

def func1(*args) :
    for i in args :
        print(i)

print("Printing values")
func1(20,40,60)
print("Printing values")
func1(80,100)

print("----------")
#exe_3

def calculation(a, b):
    addition = a + b
    subtraction = a - b 

    return(addition,subtraction)
res = calculation(40, 10)
print(res)

print("----------")
#exe_4

def showEmployee(name, salary = 9000) : 
    print("Name:",name," salary:",salary)

showEmployee("Ben", 12000)
showEmployee("Jessa")

print("----------")
#exe_5

def out_fun(a,b) : 
    
    def in_fun(a,b) : 
        add = a + b
        return (add)

    res = in_fun(a,b)
    return res + 5

res = out_fun( 3, 6)
print(res)

print("----------")
#exe_6

def add(num) :
    count = 0
    for i in range (num+1):
        count += i
        print(count)

add(10)

print("----------")
#exe_7

def display_student(name, age):
    print(name, age)

display_student("Emma", 26)

showstudent = display_student

showstudent("Emma", 26)

print("----------")
#exe_8

def rangelist(num) :
    print(list(num))

rangelist(range(4 ,30 ,2 ))

print("----------")
#exe_9

def listmax(num) :
    print(max(num))

x = [4 ,6 ,8 ,24 ,12 ,2 ]
listmax(x)
