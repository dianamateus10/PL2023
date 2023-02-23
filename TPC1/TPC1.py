import csv
import sys
import pandas as pd
from distfit import distfit
import numpy as np
import matplotlib.pyplot as plt

def distFunction(sickPeople, column, bins):
    #stores the values of the column
    value_counts = sickPeople[column].value_counts()
    #calculates the total number of indexes
    total_count = value_counts.sum()
    #creates a new dataframe for the distribution with the counts and percentages
    distribution = pd.DataFrame({'Ranges': value_counts.index.sort_values(), 'Count': value_counts.values, 'Frequency': round(value_counts / total_count, 4)})
    #removes all distributions equal to zero
    distribution = distribution[distribution['Count'] != 0]
    #sorts the intervals values
    distribution = distribution.sort_values('Ranges', ascending=True)
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
    #creates a new column with the designated colesterol group for each entry of the dataset
    lines['colesterolDist'] = pd.cut(lines['colesterol'], groups)
    #goes throught the dataframe and searches for the sick people
    sickPeople = lines[lines['temDoença'] == 1]
    #prints the distribution table
    print("Distribution of sick people by colesterol levels groups")
    distFunction(sickPeople, 'colesterolDist', bins)

def ageGroups(lines):
    #creates the ranges, not bounded on the right
    bins = list(range(25,85,5))
    groups = pd.IntervalIndex.from_breaks(bins,closed = 'left')
    #creates a new column with the designated age group for each entry of the dataset
    lines['idadeDist'] = pd.cut(lines['idade'], groups)
    #goes throught the dataframe and searches for the sick people
    sickPeople = lines[lines['temDoença'] == 1]
    #prints the distribution table
    print("Distribution of sick people by age groups")
    distFunction(sickPeople, 'idadeDist', bins)

def printDist(list, distMale, distFemale):
    #prints the frequencies and counts
    print("Value    "   + "Count    "  +  "Frequency")
    print("  M      "   +  str(list[0])  + "      " + str(distMale))
    print("  F       "   +  str(list[1])  + "      " + str(distFemale))
    #print("A distribuição de homens com doença é de " + str(distMale))
    #print("A distribuição de mulheres com doença é de " + str(distFemale))
    
      
def genderDist(lines):
    #creates a list to count how many sick people are in each gender
    l = [0,0]
    total = 0
    #goes throught the dataframe and counts the sick males and females
    for x in range(0, len(lines.index)):
        if ((lines.iloc[x]['temDoença'] == 1) and (lines.iloc[x]['sexo']) == 'M'): 
            l[0] += 1
            total += 1
        elif ((lines.iloc[x]['temDoença'] == 1) and (lines.iloc[x]['sexo']) == 'F'): 
            l[1] += 1
            total += 1
    #calculates the percentages of sick males and females
    distMale = round(l[0]/total, 4)
    distFemale = round(l[1]/total, 4)
    #prints the distribution table
    printDist(l, distMale, distFemale)

    plt.bar(['M', 'F'], [l[0], l[1]])
    plt.xlabel("Gender")
    plt.ylabel("Number of sick people")
    plt.show()
    

with open('myheart.csv') as csv_file:
    #ex.1, 2
    lines = pd.read_csv('myheart.csv')
    #ex.3, 6, 7
    genderDist(lines)
    #ex.4, 6, 7
    ageGroups(lines)
    #ex.5, 6, 7
    #colesterolGroups(lines)