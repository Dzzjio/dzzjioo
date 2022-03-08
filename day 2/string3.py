age = int(input("enter your age here: "))
name = input("enter your name here: ")
surname = input("enter yourr surname here: ")

my_text = " my name is {} my surname is {} i am {} years old"


print(my_text.format(name, surname, age))



num = int(input("enter number: "))

if num % 2 == 0:

    print("even")

else:

    print("odd")