# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:42:22 2020

@author: Happy
"""

import os 
import sys
count = 0
line_count = 0
lines_10 = []

file_arg = sys.argv[1]

with open(file_arg,'r') as file:
    lines = file.readlines()
    for line in lines:
        if(lines_10.__len__()<10):
            lines_10.append(line)
        else:
            count += 1
            file_name = "Data_10_"+count.__str__()+".csv"
            with open(file_name,"w") as wfile:
                wfile.writelines(lines_10)
            lines_10.clear() 
            command = 'conda activate base & python email_filter.py '+file_name
            os.system('start cmd /c '+'"'+command+'"')