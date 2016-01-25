# -*- coding: utf-8 -*-
print "HW2 - [FG-491 Spring 2016 Bharati Patidar]"
print "Program: fizzbuzz.py"
print "Problem Stmt:  Write a python program called fizzbuzz.py that accepts an integer n from the command line. Pass this integer to a function called fizzbuzz. The fizzbuzz function should then iterate from 1 to n. If the ith number is a multiple of two, print “fizz”, if a multiple of three print “buzz”, if a multiple of both print “fizzbuzz”, else print the value."


def fizzbuzz(num):
    #Iterates from 1 to n ( includes n)
    for i in range (1,num+1):
        
        if i%6==0:
            #Represents its a multiple of both 2 and 3 by using mod function.
            print "fizzbuzz"
            
        elif i%2==0:
            #Multiple of 2 only
            print "fizz"
        
        elif i%3==0:
            #Multiple of 3 only
            print "buzz"
        else:
            #Neither multiple of 2 nor 3
            print i

while True:

    input = raw_input("If you want to quit, say 'stop' in the input.  \nEnter an integer as input: ")
    
    #Program must exit on stop input
    if input == 'stop':
        print "Exiting from the program."
        break
    try:
        num=int(input)
        fizzbuzz(num)
        break        
    except:
        print "Error: Pls enter a valid integer only for this program."
    
        