import pandas as pd
import datetime
from datetime import timedelta
from tabulate import tabulate
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#This function loads file from directory and if needed
#deletes old stock data making room for current update


def clear_mail():
    with open('stan.txt', 'r+') as f:
        t = f.read()
        to_delete = yesterday.strip()
        f.seek(0)
        for line in t.split('\n'):
            if line != to_delete:
                f.write(line + '\n')
        f.truncate()

now = datetime.datetime.now() - timedelta(1)
yesterday = "9.11.2018"
#yesterday = now.strftime("%d.%m.%Y")
date = "10.11.2018"
df = pd.read_excel('stan.xlsx')
df = df.fillna(0)
df1 = df.loc[df["DATA"] == date]
output = df1.to_dict(orient='list')
table = tabulate(output, tablefmt = "grid", headers = "keys")



clear_mail()

stan = open("stan.txt", "a")
stan.write("\n")
stan.write(table)
stan.close()
#df.to_csv(w'/Volumes/HDD/Python/stan.txt', df1)
