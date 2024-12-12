import streamlit as st
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

#number of orders per unique modifier stored into a dictionary for each month (completed)
Parent_Menu_Selection_october_dict = {} 
Parent_Menu_Selection_september_dict = {}
Parent_Menu_Selection_august_dict = {} 
Parent_Menu_Selection_april_dict = {} 
Parent_Menu_Selection_may_dict = {}
Parent_Menu_Selection_june_dict = {} 
Parent_Menu_Selection_july_dict = {} 



#Sorting data into a list 
april_data = open('april_2024.csv', 'r')
april_data_String = april_data.read()
april_data_List = april_data_String.split('\n')
for i in range(len(april_data_List)):
    april_data_List[i] = april_data_List[i].split(',') 
april_data_List.pop(0)
april_data_List.pop(len(april_data_List)-1)


august_data = open('august_2024.csv', 'r')
august_data_String = august_data.read()
august_data_List = august_data_String.split('\n')
for i in range(len(august_data_List)):
    august_data_List[i] = august_data_List[i].split(',') 
august_data_List.pop(0)
august_data_List.pop(len(august_data_List)-1)


july_data = open('july_2024.csv', 'r')
july_data_String = july_data.read()
july_data_List = july_data_String.split('\n')
for i in range(len(july_data_List)):
    july_data_List[i] = july_data_List[i].split(',') 
july_data_List.pop(0)
july_data_List.pop(len(july_data_List)-1)


june_data = open('june_2024.csv', 'r')
june_data_String = june_data.read()
june_data_List = june_data_String.split('\n')
for i in range(len(june_data_List)):
    june_data_List[i] = june_data_List[i].split(',') 
june_data_List.pop(0)
june_data_List.pop(len(june_data_List)-1)


may_data = open('may_2024.csv', 'r')
may_data_String = may_data.read()
may_data_List = may_data_String.split('\n')
for i in range(len(may_data_List)):
    may_data_List[i] = may_data_List[i].split(',') 
may_data_List.pop(0)
may_data_List.pop(len(may_data_List)-1)


october_data = open('october_2024.csv', 'r')
october_data_String = october_data.read()
october_data_List = october_data_String.split('\n')
for i in range(len(october_data_List)):
    october_data_List[i] = october_data_List[i].split(',')
october_data_List.pop(0) 
october_data_List.pop(len(october_data_List)-1)


september_data = open('september_2024.csv', 'r')
september_data_String = september_data.read()
september_data_List = september_data_String.split('\n')
for i in range(len(september_data_List)):
    september_data_List[i] = september_data_List[i].split(',') 
september_data_List.pop(0) 
september_data_List.pop(len(september_data_List)-1)


allMonths_data = []
allMonths_data = april_data_List + may_data_List + june_data_List + july_data_List + august_data_List + september_data_List + october_data_List 



Order_num = 0
Sent_Date = 1
Modifier = 2
Option_Group_Name = 3
Parent_Menu_Selection = 4
Order_ID_Indexes = 5


for entry in april_data_List:
    item = entry[2]
    if item in Parent_Menu_Selection_april_dict:
        Parent_Menu_Selection_april_dict[item] += 1
    else:
        Parent_Menu_Selection_april_dict[item] = 1

for entry in may_data_List:
    item = entry[2]
    if item in Parent_Menu_Selection_may_dict:
        Parent_Menu_Selection_may_dict[item] += 1
    else:
        Parent_Menu_Selection_may_dict[item] = 1

for entry in june_data_List:
    item = entry[2]
    if item in Parent_Menu_Selection_june_dict:
        Parent_Menu_Selection_june_dict[item] += 1
    else:
        Parent_Menu_Selection_june_dict[item] = 1

for entry in july_data_List:
    item = entry[2]
    if item in Parent_Menu_Selection_july_dict:
        Parent_Menu_Selection_july_dict[item] += 1
    else:
        Parent_Menu_Selection_july_dict[item] = 1

for entry in august_data_List:
    item = entry[2]
    if item in Parent_Menu_Selection_august_dict:
        Parent_Menu_Selection_august_dict[item] += 1
    else:
        Parent_Menu_Selection_august_dict[item] = 1

for entry in september_data_List:
    item = entry[2]
    if item in Parent_Menu_Selection_september_dict:
        Parent_Menu_Selection_september_dict[item] += 1
    else:
        Parent_Menu_Selection_september_dict[item] = 1

for entry in october_data_List:
    item = entry[2]
    if item in Parent_Menu_Selection_october_dict:
        Parent_Menu_Selection_october_dict[item] += 1
    else:
        Parent_Menu_Selection_october_dict[item] = 1

