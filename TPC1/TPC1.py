import csv
import sys
import pandas as pd
from distfit import distfit
import matplotlib.pyplot as plt


def distFunction(lines, column, bins=10):
    value_counts = lines[column].value_counts()
    total_count = value_counts.sum()
    distribution = pd.DataFrame({'Value': value_counts.index, 'Count': value_counts.values, 'Percentage': round(value_counts / total_count * 100, 2)})
    distribution = distribution[distribution['Count'] != 0]
    distribution = distribution.sort_values('Count', ascending=False)
    print(distribution.to_string(index=False))

    if(column == 'sexo'):
        fig, ax = plt.subplots()
        ax.bar(distribution['Value'], distribution['Count'])
        ax.set_title("Distribution of " + column  + "in sick people")
        ax.set_xlabel("Value")
        ax.set_ylabel("Count")
        plt.show()
    else:
        plt.hist(distribution['Count'], bins)
        plt.xlabel(column)
        plt.title(f'{column} Distribution in sick people')
        plt.show()

def colesterolGroups(lines):
    #checks the colesterol minimum and maximum values
    min_series = lines.min()
    max_series = lines.max()
    colesterol_min = min_series[3]
    colesterol_max = max_series[3]
    #creates the ranges, not bounded on the right
    bins = list(range(colesterol_min,colesterol_max+10,10))
    #goes throught the dataframe and searches for the sick people
    for x in range(0, len(lines.index)):
        if((lines.iloc[x]['temDoença']) == 1):
            groups = pd.IntervalIndex.from_breaks(bins,closed = 'left')
            #creates a new column with the designated colesterol group for each entry of the dataset
            lines['colesterolDist'] = pd.cut(lines['colesterol'], groups)
    distFunction(lines, 'colesterolDist', bins)
    #counts the number of people in each colesterol group
    #colesterol_counts = lines['colesterolDist'].value_counts()
    #removes the colesterol groups with no counts
    #colesterol_counts = colesterol_counts[colesterol_counts != 0]
    #calculates the percentage of people in each colesterol group
    #colesterol_percentages = round(colesterol_counts/colesterol_counts.sum() * 100, 2)
    #prints both
    #print(colesterol_counts)
    #print(colesterol_percentages)

def ageGroups(lines):
    #creates the ranges, not bounded on the right
    bins = list(range(25,85,5))
    #goes throught the dataframe and searches for the sick people
    for x in range(0, len(lines.index)):
        if((lines.iloc[x]['temDoença']) == 1):
            groups = pd.IntervalIndex.from_breaks(bins,closed = 'left')
            #creates a new column with the designated age group for each entry of the dataset
            lines['idadeDist'] = pd.cut(lines['idade'], groups)
    distFunction(lines, 'idadeDist', bins)
    #counts the number of people in each age group
    #age_counts = lines['idadeDist'].value_counts()
    #calculates the percentage of people in each age group
    #age_percentages = round(age_counts/age_counts.sum() * 100, 2)
    #prints both
    #print(age_counts)
    #print(age_percentages)
    
      
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
    #prints the percentages
    print("A distribuição de homens com doença é de " + str(distMale) + "%")
    print("A distribuição de mulheres com doença é de " + str(distFemale) + "%")

with open('myheart.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lines = pd.read_csv('myheart.csv')
    #genderDist(lines)
    distFunction(lines, 'sexo')
    ageGroups(lines)
    colesterolGroups(lines)
