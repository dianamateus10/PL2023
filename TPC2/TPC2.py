import csv
import sys
import pandas as pd
from distfit import distfit
import numpy as np
import matplotlib.pyplot as plt

def digitSum(line):
    total = 0
    #goes throught the list
    for x in line:
        for y in x:
            if (y.isdigit() == True): total += int(y)
    print (total)

#ex.2
def exercise2():
    for line in sys.stdin:
        print(line)
        

#ex.3, 4, 5
def stringComp():
    numberLines = input("Give the number of lines ")
    string = ""
    for i in numberLines:
        for line in sys.stdin:
            newline = line.rstrip()
            string = string + newline
            if (newline.lower() == 'off'):
                break
            elif (newline.lower() == '='): 
                digitSum(string)
            #elif(newline.lower() == 'on'):

#ex.1
with open('text.txt', 'r') as file:
    #reading the lines in the file
    lines = file.readlines()
    digitSum(lines)

stringComp()
#exercise2()