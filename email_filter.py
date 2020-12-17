# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 07:27:23 2020

@author: Happy
"""
import sys
import os
from validate_email import validate_email

data_file = sys.argv[1]

count = 0
with open("verified_emails.csv","a") as write_file:
    with open(data_file,"r") as read_file:
        lines = read_file.readlines()
        for email in lines:
            count +=1
            email=email.strip()
            is_valid = validate_email(email, check_regex=True, check_mx=True, from_address='rambir.git@gmail.com', helo_host='my.host.name', smtp_timeout=10, dns_timeout=10, use_blacklist=True, debug=False)
            print(count.__str__()+". "+email+" is valid? "+is_valid.__str__())
            if(is_valid):
                write_file.writelines(email+"\n")

os.remove(data_file)