Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #FizzBuzz is a well known programming assignment, asked during interviews.

#The given code solves the FizzBuzz problem and uses the words "Solo" and "Learn" instead of "Fizz" and "Buzz".
#It takes an input n and outputs the numbers from 1 to n.
#For each multiple of 3, print "Solo" instead of the number.
#For each multiple of 5, prints "Learn" instead of the number.
#For numbers which are multiples of both 3 and 5, output "SoloLearn".
>>> 
>>> n = int(input())

for x in range(1, n,2):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
        continue
    elif x % 3 == 0:
        print("Solo")
        continue
    elif x % 5 == 0:
        print("Learn")
        continue
    else:
        print(x)