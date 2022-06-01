# -*- coding: utf-8 -*-
"""
Created on Tue May 24 12:37:45 2022

@author: jario
"""
import csv
import pandas as pd
import matplotlib.pyplot as plt

#Creamos archivo
row_list = [["SN", "Nombre", "Contribucion","Patrimonio","Edad"],
             [1, "Linus Torvalds", "Linux Kernel",66.000,52],
             [2, "Tim Berners-Lee", "World Wide Web",45.000,66],
             [3, "Mark Zuckerberg", "Facebook",73.000,38],
             [4, "Guido van Rossum", "Python Programming",189.000,66],
             [5, "Jeff Bezos", "Amazon",240.000,58]]

with open('archivo.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)
    
#Metodo para crear archivo parquet
def write_parquet_file():
    df = pd.read_csv('./archivo.csv')
    df.to_parquet('./archivo_final.parquet')
    
write_parquet_file()
print("Archivo escrito", "----->","archivo_final.parquet")