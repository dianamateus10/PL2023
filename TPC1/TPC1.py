import csv
import sys
import pandas as pd
from distfit import distfit
import matplotlib.pyplot as plt


def distFunction(lines, column):
    #stores the values of the column
    value_counts = lines[column].value_counts()
    #sums all the values (to find the total number of indexes)
    total_count = value_counts.sum()
    #creates a new dataframe for the distribution with the counts and percentages
    distribution = pd.DataFrame({'Value': value_counts.index.sort_values(), 'Count': value_counts.values, 'Percentage': round(value_counts / total_count * 100, 2)})
    #removes all distributions equal to zero
    distribution = distribution[distribution['Count'] != 0]
    #sorts the intervals values
    distribution = distribution.sort_values('Count', ascending=False)
    #prints the distribution table
    print(distribution.to_string(index=False))


def colesterolGroups(lines):
    #checks the colesterol minimum and maximum values
    min_series = lines.min()
    max_series = lines.max()
    colesterol_min = min_series[3]
    colesterol_max = max_series[3]
    #creates the ranges, not bounded on the right
    bins = list(range(colesterol_min,colesterol_max+10,10))
    groups = pd.IntervalIndex.from_breaks(bins,closed = 'left')
    #goes throught the dataframe and searches for the sick people
    for x in range(0, len(lines.index)):
        if((lines.iloc[x]['temDoença']) == 1):
            #creates a new column with the designated colesterol group for each entry of the dataset
            lines['colesterolDist'] = pd.cut(lines['colesterol'], groups)
    #prints the distribution table
    print("Distribution of sick people by colesterol levels groups")
    distFunction(lines, 'colesterolDist')

def ageGroups(lines):
    #creates the ranges, not bounded on the right
    bins = list(range(25,85,5))
    groups = pd.IntervalIndex.from_breaks(bins,closed = 'left')
    #goes throught the dataframe and searches for the sick people
    for x in range(0, len(lines.index)):
        if((lines.iloc[x]['temDoença']) == 1):
            #creates a new column with the designated age group for each entry of the dataset
            lines['idadeDist'] = pd.cut(lines['idade'], groups)
    #prints the distribution table
    print("Distribution of sick people by age groups")
    distFunction(lines, 'idadeDist')

def printDist(list, distMale, distFemale):
    #prints the percentages
    print("Value    "   + "Count    "  +  "Percentage of the gender with sickness")
    print("  M      "   +  str(list[0])  + "      " + str(distMale) + "%")
    print("  F       "   +  str(list[1])  + "      " + str(distFemale) + "%")
    #print("A distribuição de homens com doença é de " + str(distMale) + "%")
    #print("A distribuição de mulheres com doença é de " + str(distFemale) + "%")
    
      
def genderDist(lines):
    #creates a list to count how many sick people are in each gender
    list = [0,0]
    #counts how many female and males are on the dataser
    gender = lines['sexo'].value_counts()
    #goes throught the dataframe and counts the sick males and females
    for x in range(0, len(lines.index)):
        if ((lines.iloc[x]['temDoença'] == 1) and (lines.iloc[x]['sexo']) == 'M'): list[0] += 1
        elif ((lines.iloc[x]['temDoença'] == 1) and (lines.iloc[x]['sexo']) == 'F'): list[1] += 1
    #calculates the percentages of sick males and females
    distMale = round(list[0]/gender[0] * 100, 2)
    distFemale = round(list[1]/gender[1] * 100, 2)
    #prints the distribution table
    printDist(list, distMale, distFemale)
    

with open('myheart.csv') as csv_file:
    #ex.1,2
    csv_reader = csv.reader(csv_file, delimiter=',')
    lines = pd.read_csv('myheart.csv')
    #ex.3, 6, 7
    genderDist(lines)
    #ex.4, 6, 7
    ageGroups(lines)
    #ex.5, 6, 7
    colesterolGroups(lines)
