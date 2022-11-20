import os
import math
import random
import smtplib
import xmlrpc.client
import json

# SENDING EMAIL NOTIFICATION FOR THE USER AUTHENTICATION
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("husseinkatana17@gmail.com", "rpxjiaxewfyjmcvl")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")

# IR.MAIL_SERVER


# CONNECT TO THE ODOO DATABASE FOR THE LOGIN ACCESS
url = "http://localhost:8069"
db = "v15"
username = "hussein@gmail.com"
password="Depx@$eaNt(Z2%Y3"
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
AUTHORIZATIONS = common.authenticate(db, username, password, {})

if AUTHORIZATIONS:
    print(AUTHORIZATIONS,"KADWEKA")
else:
    print('YOUR NOT AUTHORIZED!')