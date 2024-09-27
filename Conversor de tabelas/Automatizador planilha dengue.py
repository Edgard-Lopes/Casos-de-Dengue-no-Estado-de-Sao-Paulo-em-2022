# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 21:04:30 2023

@author: edgar
"""
from unidecode import unidecode
import pandas as pd
import csv
fields = [            
            "Id_DRS",
            "DRS",
#            "ESTADO",
            "ID_GVE",
            "GVE",
            "ID_RdS",
            "RdS",
            "Id_Município",
            "Município",
            "Data", #esse é especial, tem que criar
            "notificados",
            "confirm_autoc",
            "confirm_import"]
head_lines = {            
            "Id_DRS": [],       #posição 0
            "DRS": [],          #posição 1
            # "ESTADO": [],
            "ID_GVE": [],       #posição 2
            "GVE": [],          #posição 3
            "ID_RdS": [],       #posição 4
            "RdS": [],          #posição 5
            "Id_Município": [], #posição 6
            "Município": [],    #posição 7
            }
head_lines_part2 = {
        "data": [], #append 01/01/2023, 01/02/2023, etc. Ude a variável date
        "notificados": [], #8,11,14, etc
        "confirm_autoc": [],
        "confirm_import":  []
        }


file_path = "C:/Users/edgar/Downloads/Power BI"
file = "sitedenguejan.dez.2022.entrega13.02.23.xlsx%3Fattach=true2.csv"
with open(file_path+"/"+file, "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    list =[]
    for i, linha in enumerate(arquivo_csv):
        list.append(str(linha))
date = (file.split("."))[2]

count = 0
while count < 5:          
    del list[0]
    del list[-1]
    count = count + 1
while count < 6:          
    del list[-1]
    count = count + 1

#print(list[0])
#print(list[0][:-17])
#print(list[-1])
#print(list[-1][:-17])

final_line = []
#print(list[0])
counter = 0
for lista in list:
    x = list[counter][:-17] #criar um define
    counter = counter + 1
    #x = list[0][:-17] #criar um define
    
    x = x[2:]
    x = x.split(";")
    y = x[6]
    Id_Munic = [y[0:5]]
    Munic = [y[7:]]
    # y = x[6].split(" ")
    #print(y)
    final_line = x[0:6] + Id_Munic + Munic + x[7:-3] #remove as 3 últimas colunas que estão com as somas
    """for x in final_line:
        count = count + 1
    print(count)"""
    "print(final_line)"
    #print(x)
    lines = []
    item = 0
    
    count = 0
    while count <12:
        for k, value in head_lines.items(): 
                lines = value
                lines.append(final_line[item])
                        #print(lines)
                        #lines
                head_lines[k] = lines
                if item == 7:
                    item = 0;
                else:
                    item = item + 1
        
    
        lines = head_lines_part2["data"] 
        lines.append("1"+"/"+ str(count+1) + "/"+ date)
        head_lines_part2["data"] = lines #append 01/01/2023, 01/02/2023, etc. Ude a variável date
        multiplier = count*3
        #print(head_lines_part2["notificados"])
        lines = (head_lines_part2["notificados"])
        lines.append(final_line[8+multiplier])
        head_lines_part2["notificados"] = lines #8,11,14, etc count*3
        lines = (head_lines_part2["confirm_autoc"])
        lines.append(final_line[9+multiplier])
        head_lines_part2["confirm_autoc"]  = lines
        lines = (head_lines_part2["confirm_import"])
        lines.append(final_line[10+multiplier])
        head_lines_part2["confirm_import"] = lines
        
        count = count + 1
#print(head_lines_part2)

#print(head_lines)
#print(x)


#print(pd.DataFrame(head_lines))
#print(pd.DataFrame(head_lines_part2))

list_strings = ["DRS","GVE","RdS","Município"]
for item in list_strings:
    z =[]
    x = head_lines.get(item)
    for string in x:
        y = unidecode(string)
        z.append(y)
    print(z[17:24])
    head_lines[item] = z


head_lines.update(head_lines_part2)
# print(pd.DataFrame(head_lines))

file = file[:-23] + "convertido" + ".csv"
print("Abrindo arquivo: ", file)

pd.DataFrame(head_lines).to_csv(file, mode = 'w')
print("arquivo criado ou atualizado.")

# =============================================================================
# pd.DataFrame(head_lines).to_csv(path_or_buf=None, sep=',', na_rep='', float_format=None, 
#                  columns=None, header=True, index=True, index_label=None, mode='w', 
#                  encoding=None, compression='infer', quoting=None, quotechar='"', 
#                  lineterminator=None, chunksize=None, date_format=None, doublequote=True,
#                  escapechar=None, decimal='.', errors='strict', storage_options=None)
# =============================================================================

# =============================================================================
# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# 
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
# =============================================================================
# =============================================================================
# with open(file_path+"/"+file, "w") as cvsfile:
#     field = fields
#     writer = csv.DictWriter(cvsfile, fieldnames = field)
#     writer.writeheader()
#     writer.writerow({"Id_DRS": 'Baked', 'DRS': 'Beans'})
# =============================================================================
# =============================================================================
# f = open(file_path+"/"+file, "w")
# writer = csv.DictWriter(f, fieldnames = fields)
# writer.writeheader() 
# writer.writerows(head_lines)
# =============================================================================

# =============================================================================
# try:
#     open(file_path+"/"+file, "r")            
# except:
#     print("Não há arquivo com esse nome: \n Criando um arquivo...")
# else:
#     f = open(file_path+"/"+file, "w", newline = " ")
#     writer = csv.DictWriter(f, fieldnames = fields)
#     writer.writeheader() 
#     writer.writerows(head_lines)
# =============================================================================

