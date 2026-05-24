#input()= A function that allows the user to input data into the program. It takes a string as an argument, which is displayed as a prompt to the user. The function then waits for the user to enter some data and press the Enter key. Once the user has entered their input, it is returned as a string.

# input() returns a string

input_name = input("Enter your name: ")

# Convert input to integer
input_age = int(input("Enter your age: "))

# Now arithmetic works
input_age = input_age + 1
# or
# input_age += 1

print("Your name is:", input_name)
print("Your age next year will be:", input_age)


#calculate the area of rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("The area of the rectangle is:", area,"cm^2")

#shopping cart
item1 = input("Enter the name of the first item: ")
price1 = float(input("Enter the price of the first item: "))
item2 = input("Enter the name of the second item: ")
price2 = float(input("Enter the price of the second item: "))
total_price = price1 + price2
print(f"The total price of {item1} and {item2} is: ${total_price:.2f}")
