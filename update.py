import pandas as pd
import datetime
from datetime import timedelta
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#This function loads file from directory and if needed
#deletes old stock data making room for current update

def clear_mail():
    f = open("stan.txt", "r")
    lines = f.readlines()
    f.close()
    f = open("stan.txt", "w")
    for line in lines:
        if line != yesterday:
            f.write(line)
    f.close()

now = datetime.datetime.now() - timedelta(1)
yesterday = "28.11.2018"
#yesterday = now.strftime("%d.%m.%Y")
date = "29.11.2018"
df = pd.read_excel('stan.xlsx')
df = df.fillna(0)
#print(df.loc[df["DATA"] == date])
df1 = df.loc[df["DATA"] == date]
output = df1.to_dict()
clear_mail()

stan = open("stan.txt", "a")
stan.write("\n")
stan.write()
stan.close()
#df.to_csv(w'/Volumes/HDD/Python/stan.txt', df1)
