# -*- coding: utf-8 -*-
"""
Created on Sun May 22 14:40:24 2022

@author: jario
"""
import pandas as pd
import pyorc
import findspark
from pyspark.sql import SparkSession
 
#Lectura del archivo 
with open("./archivo.orc", "rb") as data:
    reader = pyorc.Reader(data)
    print("Sin el Dataframe de pandas\n")
    for row in reader:
        print(row)
        
#Dataframe pandas
findspark.init()
spark = SparkSession.builder.getOrCreate()
df_spark = spark.read.orc('./archivo.orc')
df_pandas = df_spark.toPandas()
df_pandas.rename(columns={'col0': 'servername', 'col1': 'lastping', 'col2':'status'}, inplace=True)
print("\nDataframe de pandas")
print("\n",df_pandas)
    

