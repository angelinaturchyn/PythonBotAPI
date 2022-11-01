from main import print_hi

if __name__ == "__app__":
    print_hi('PyCharm')

print("Hello World")
age = 20
price = 19.95
first_name = "Angelina"
is_online = False
print(first_name)

name = input("What is your name girl? ")
##after running command type your name next to it than run the file again
print("Hello " + name)

birth_year = input("Enter your birth year: ")
age = 2022 - int(birth_year)  ##convert string to a number int
print(age)

first_number = input("First: ")
second_number = input("Second: ")
sum_of_numbers = float(first_number) + int(second_number)
print("Sum:" + str(sum_of_numbers))


str()