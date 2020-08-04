import sys

num = sys.argv[1]
result = 1


def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            global result
            result = 0


isPrime(int(num))
if (result == 1):
    print("true")
else:
    print("false")
