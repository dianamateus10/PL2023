import csv
import sys
import pandas as pd
from distfit import distfit
import numpy as np
import matplotlib.pyplot as plt

"""
Partindo do dataset alunos.csv
1. Leia e imprima todas as entradas do ficheiro csv
2. Crie uma função que verifique quantas linhas tem o ficheiro
3. Crie um dicionário para albergar todas as informações relativas a um aluno com o formato
{ id_aluno: [notas: [TPC1, TPC2, TPC3, TPC4], nome: NOME, curso: CURSO]}
3.1 Quais os alunos com melhor média?
3.2 Quantos alunos de LEI tem a média dos TPCs superior a 15?
"""
class alunos:
    def loadData(csv_file):
        #opening the file
        with open(csv_file, 'r') as file:
            #variable to count the number of lines
            lines = 0
            csvreader = csv.reader(file)
            #go through all the lines and print them as well as count them
            for row in csvreader:
                print(row)
                lines += 1
            #print the total number of lines
            print("this is the number of lines: " + str(lines))
    def alunoDic(csv_file):

alunos.loadData("./alunos.csv")
alunos.alunoDic("./alunos.csv")

"""
Regular Expressions
"""
