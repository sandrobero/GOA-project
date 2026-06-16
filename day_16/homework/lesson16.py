# slicing-სიიდან კონკრეტული მონაკვეთის გამოტანას გვაძლევს

fruits=["ვაშლი", "ბანანი", "ატამი", "მსხალი", "ალუბალი"] 

print(fruits[2])

numbers = [10, 20, 30, 40, 50]

numbers[1] = 25

print(numbers)

colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]

num=int(input("enter number: "))

print(colors[num])

animals = ["ძაღლი", "კატა", "სპილო", "ვეფხვი", "ლომი"]

animals[-1] = "გემი"

print(animals)

colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"] 

num1=int(input("enter number: "))

num2=str(input("enter color: "))

colors[num1] = num2

print(colors)

numbers_step = [5, 10, 15, 20, 25, 30, 35, 40] 

print(numbers_step[0::2])

fruits = ["ვაშლი", "მსხალი", "ატამი", "ბალი", "ყურძენი", "ბანანი", "ფორთოხალი"]

print(fruits[2:5])

mixed_nums = [12, 45, 8, 33, 91, 24, 10, 77]

for i in mixed_nums:
    if i % 2==0:
        print(i)





