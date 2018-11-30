import pandas as pd
import datetime
from datetime import timedelta
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
now = datetime.datetime.now()
today = now.strftime("%d.%m.%Y")


df = pd.read_excel('stan.xlsx')
df = df.fillna(0)
print(df.loc[df["DATA"] == today])
