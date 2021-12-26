#Write your code below this row 👇

for n in range(1, 101):
    #need both first because it doesn't go back to check again
    if n % 3 ==0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    #what should the rest do?
    else:
        print(n)