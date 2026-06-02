num=13

if num < 10:
    print("less than 10")
else:
    print("more than 10")


age=int(input("enter your age: "))

if age == 15:
    print("equal to 15")
else:
     print("not equals to 15")

word=(input("enter word: "))


if word==("group92"):
    print("you are correct ❤")
else:
    print("you are wong!!")

for i in range(50,100,5):
    print(i)

name=("sandro bero")

for  i in name:
    print(i)


number = 20

while number <= 50:
    print(number)
    number += 1  

for i in range(100):
    print(i)

num=0

while num<=99:
    print(num)
    num+=1

for i in range(101):
    print(i)

num1=0

while num1<=100:
    print(num1)
    num1+=1

for i in range(10,20):
    print(i)

num3=0

while num3<=20:
    print(num3)
    num3+=1

for i in range (10,20,5):
    print(i)

num4=10

while num4<=20:
    print(num4)
    num4+=5

for i in range(100,201):
    print(i)

num5=100
while num5<=200:
   print(num5)
   num5+=1

for i in range(11,-1,-1):
    print(i)

num6=10

while num6 >= 0:
    print(num6)
    num6 -= 1

ricxvi=int(input("enter a number: "))
if ricxvi > 1:
    print("es ricxvi dadebitia")
elif ricxvi < 1:
    print("es ricxvi uaryofilia")
else:
    print("es ricxvi nulia")

age1=int(input("enter age: "))

if age1< 0:
    print("araswori info")
elif age1 <= 12:
    print("bavshvi xar")
elif age1 <= 19:
    print("mozardi/tineijeri xar")
elif age1 <= 64:
    print("zrdasruli xar")
elif age1 <= 120:
    print("xanshi shesuli xar")
else:
    print("guru an jadoqari xar")

num1 = int(input("enter 1 number: "))
num2 = int(input("enter 2 number: "))
num3 = int(input("enter 3 number: "))


if num1 >= num2 and num1 >= num3:
    biggest = num1

elif num2 >= num1 and num2 >= num3:
    biggest = num2

else:
    biggest = num3

print("biggest number is:", biggest)

word=int(input("enter num: "))
if word==1:
    print("orshabati")
if word==2:
    print("samshabati")
elif word==3:
    print("otxshabati")
elif word==4:
    print("xutshabati")
elif word==5:
    print("paraskevi")
elif word==6:
    print("shabati")
elif word==7:
    print("kvira")
else: 
    print("es ar vici ra dgea")

word1=int(input("enter number: "))

if word1 > 50:
    shedegi=word1*5
    print("sheni ricxvi metia 50-ze")
else:
    shedegi=word1**5
    print("sheni ricxvi ar aris meti 50-ze")

password=str(input("enter password: "))

if password==("goa123"):
    print("password is correct!")
else:
    print("password is incorrect")


user_number = int(input("shemoiyvale ricxvi: "))


total_sum = 0

for i in range(1, user_number + 1):
    total_sum += i 

print("ricxvebis jami:", total_sum)


for ticket in range(1, 5001):
    

    if ticket == 2024:
        print("bileti ar aris  napovni")
        break 
        

    print("bileti napovnia")



for number in range(1, 301):

    if number % 4 == 0 and number % 7 == 0:
        print(f"pasuxi: {number}")
        break  


for number in range(1, 51):
    
   
    if number % 10 == 0:
        continue 
      
    print(number)



