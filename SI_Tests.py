#A simple program to find the root of a number using either the newton method, bisection method, or fixed-point method in calculus
#Please make sure to edit your function and derivitive values as the program is simple and does not do it for you
#Author: Michael Andersen
#Made Fall 2018
import math
def newton(x):
    answer_list = []
    boolean = True
    i = 0
    while boolean:
        my_function = x**3 - 18 #This is where you edit your original function values
        my_derivitive = 3 * x**2 #This is where you edit your derivitive values
        x = x - (my_function/my_derivitive)
        result = '{:0.6g}'.format(x) #formated to 5 decimal places, edit as needed
        if result not in answer_list:
            answer_list.append(result) #addes formated value to the list in order to check for duplicate values
            i+=1
        elif result in answer_list:
            i+=1
            print(result)
            boolean = False #Once the first duplicate is found inside of the list the function stop running and displays the root of the x value


def fixed_point(x):
    i = 0
    answer_list = []
    boolean = True
    while boolean:
        x = 1.3*math.cos(x) #Make sure to edit your original function here!
        result = '{:0.6g}'.format(x)
        if result not in answer_list: #checks if the result is already in the list or not
            i+=1
            print(result) #the print is used to show values at where you are not looking for the final value but the values in between
            answer_list.append(result)
        elif result in answer_list: #if the result is in the list print out the result and stop iterating
            i+=1
            print(result)
            boolean = False


def bisection(a,b):
    error = 0.00001 #Edit your error to your liking
    x = 0
    answer_list = []
    answer_list.append(b)
    i = 1
    boolean = True
    while boolean:
        c = (a + b) / 2
        c_function = (3*c**3)-(9*c**2)+(15*c)-24 #this is where your function goes, make sure you use c and not x while writing
        if c_function < 0:
            a = c
            x =a
            answer_list.append(x)
        elif c_function >0:
            b = c
            x = b
            answer_list.append(x)
        if math.fabs(answer_list[i]-answer_list[i-1]) < error:
            result = '{:0.8g}'.format(answer_list[i])
            print(result)
            boolean = False
        i+=1


def calc():
    print("This program helps determine the root of a number")
    print("What method are you using?")
    print("1 - Bisection")
    print("2 - Fixed point")
    print("3 - Newton's")
    print("0 - Exit program")

    choice = int(input("Please enter your choice here: "))

    if choice == 1:
        a = float(input("Please enter your a value: "))
        b = float(input("Please enter your b value: "))
        bisection(a,b)
    elif choice == 2:
        x = float(input("Please enter your x value: "))
        fixed_point(x)
    elif choice == 3:
        x = float(input("Please enter your x value: "))
        newton(x)
    elif choice == 0:
        boolean = False
    else:
        print("That is not an option")
calc()