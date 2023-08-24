# Receiving value

name = input("What is your name? ")
print("Hello  " + name)


# finding age

birth_year = input("Enter your birth year ")
age = 2023 - int(birth_year)
print(age)


#some built in functions
#int()
#float()
#bool()
#str()


# adding numbers

first = input("First: ")
second = input("Second: " )
sum = int(first) + int(second)
print(sum)

# adding decimal numbers using float

first = input("First: ")
second = input("Second: ")
sum = float(first) + float(second)
print("Sum: " + str(sum))

# another solution for same problem

first = float(input("First: "))
second = float(input("Second: "))
sum = first + second
print("Sum: " + str(sum))