a=2
print(type(a))
b=2.3
print(type(b))
c=2+3j
print(type(c))
d='a'
print(type(d))
e=None
print(type(e))
f=True
print(type(f))



for i in range(1,6):
    for j in range(1,6):
        print(i*j,end="")
    print()


m=10
m_str=str(m)
print(type(m_str))
print(m_str)

m="200"
m_int=int(m)
print(m)
print(type(m_int))

m=tuple("welcome")
l=list(m)
l[0]="p"
print(l)
print(m)


print("----------------------List---------------------")

list=[1,3,5]
list.append(2)
print(list)
list.insert(1,4)
print(list)
list.remove(2)
print(list)
pop_list=list.pop(0)
print(list)
print(pop_list)

print("----------------------Set------------------------")

my_set = {1, 2, 3,1}
new_set = my_set
new_set.add(4)

print(my_set)    
print(new_set)

print("----------------------Dictionary---------------------")

my_dict = {"name": "Ram", "age": 25}
new_dict = my_dict
my_dict["age"] = 37

print(my_dict)   
print(new_dict)

print("----------------------Tuple---------------------")

my_tuple="welcome to this python language"
my_tuple[0]="T"
print(my_tuple)


Print("-------------------String------------------------")
str='hello'
print(str)
str1="world"
print(str1)
str2="""Python"""
print(str2)
print(str+str1)
print(str[0])
del str
str="Hello World"
print(str[6:11])
print("world" in str)
print("Hello" not in str)

print("-----------------------Functions------------------")
def greet(name):
    print("Hello"+name)
greet("World")

def add(num1,num2):
    sum=num1+num2
    return sum
print(add(2,3))

global_var=10
def function():
    local_var=20
    print(global_var)
    print(local_var)
function()
print(global_var)
print(local_var)





# Operations 
a=23
b=24
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

# conditional 
i = 99

if i <= 0:
    print("please enter a positive number")
elif i >= 90:
    print("1st")
elif i >= 80:
    print("2nd")
elif i >= 60:
    print("3rd")
elif i >= 35:
    print("pass")
else:
    print("Fail")
