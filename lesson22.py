# append()-ამატებს ახალ ელემენტს სიის სულ ბოლოში
# instert()-ამატებს ახალ ელემენტს სიის კონკრეტულ პოზიციაზე
# pop()-ამოღებს ელემენტს სიის ბოლოდან ან კონკრეტული პოზიციიდან

# colors = ['red', 'green', 'blue', 'yellow', 'black']

# colors=len(colors)

# print(colors)

# car=input("Enter a car: ")

# list=["mersedes", "audi","toyota"]

# list.append(car)

# print(list)

# colors = ["red", "green", "blue", "yellow", "purple"]

# colors.pop(4)

# print(colors)

# animals = ["dog", "cat", "elephant", "lion"]

# animals.insert(2, "tiger")

# print(animals)

word = input("Enter a name: ")
word1=input("Enter a name: ")
word2=input("Enter a name: ")
word3=input("Enter a name: ")

teacher = [word, word1, word2]

teacher.append(word3)

teacher.pop(3)

print(len(teacher))
print(teacher)
