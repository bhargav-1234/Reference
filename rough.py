import sys
print("hello Bhargav")
# [notice] To update, run: python.exe -m pip install --upgrade pip
a=10
print(a)
print(sys.version)
b=5
if a<b:
    print('no')
else:
    print('not posible')

MyVar=15
print(MyVar)
myVar=3
print(myVar)
my_first_Name="bhargav"
print(my_first_Name)
x,y,z="1","2","3"
print(x)
print(y)
print(z)
numbers="1","2","3"
x,y,z= numbers
print(numbers)

def fun():
    print(myVar)

fun()
y=5
def my():
    x= 10
    print(x)
my()
print(y)

# text type - str
# numerric type - int, float, complex
# mapping type - dict
# set type - set, frozenset
# boolean type - bool
# binary type - bytes, bytearray, memoryview
# none type - nonetype

#  if you want to know the type of data type we can use "type"

#  strings
firstName ="Bhargav"
lastName ="Honey"
print(firstName +" "+ lastName)

"""firstName ="Bhargav"
lastName ="Honey"                         this is called multi line string
print(firstName +" "+ lastName)"""

print(firstName[2:6])
print(len(firstName + lastName))

txt = "Bhargav is one of kindest person i know"
print("kindest" in txt)

# Slicing

print(firstName[1:6])
print(firstName[:6])
print(firstName[::-1])
print(firstName[1::])
print(firstName[-6:])

#  upper()
print(txt.upper())
# lower()
print(txt.lower())
# remove white space
A=" hello, world! "
print(A.strip())
# replace()
print(A.replace("h","M"))
# split()
print(A.split())
age=25
print(f"Bhargav age is {age}")
price=203.15
print(f"The price is {price} dollars")
print(f"The price is {price:.4f} dollars")
print(f"the sum is {50 * 20}")
print(10<25)
print(12>50)
print(3>2)

x= 5
print(x**2)
x+=2
print(x)
x-=2
print(x)
print(x*2)
print(x/3)
print(x%2)
x%=2
print(x)
x^=2
print(x)
print(x:=3)
x&=2
print(x)
x|=2
print(x)

y=25
print(y<10 and y>13)
print(y<10 or y>13)
print (not(y<10 or y>13))
print(not(y<10 and y>13))
x1=['banana','apple']
y1=['banana','apple']
z=x1
print(x1 is y1)
print(x1 is z)
print(z is y1)
print('banana' in x1)

# list

thisList=['apple','banana','cherry','apple','strawberry']
print(thisList)
thisList[0]='mango'
print(thisList)
print(len(thisList))
print(type(thisList))
list=['abc',2,'Bhargav',25,True]
print(list)
print(list[2])
print(list[-2])
print(thisList[2:5])
print(thisList[2:])
print(thisList[::-1])

if "apple" in thisList:
    print("yes, it's in the list")
else:
    print("No")

thisList[1:2]=["gao","pemogranate"]
print(thisList)
thisList.insert(2,"avocado")
print(thisList)

thisList.append("orange")
print(thisList)

thisList.pop(1)
print(thisList)
del thisList[2]
print(thisList)

for x in thisList:
    print(x)


