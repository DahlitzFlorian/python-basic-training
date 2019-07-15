# This is a possible solution for exercise_05.py
def fibonacci(number):
    i = 1

    if number == 0:
        fib = []
    elif number == 1:
        fib = [1]
    elif number == 2:
        fib = [1,1]
    elif number > 2:
        fib = [1, 1]
        while i < (number - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib


number = int(input("How many numbers should I generate for you: "))
print(fibonacci(number))
