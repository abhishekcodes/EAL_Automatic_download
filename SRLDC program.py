# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 16:22:44 2018

@author: abhishek chandel
"""

import urllib.request
import datetime
import urllib


#%y gives date in 2 digits and %Y gives data in 4 digits    
yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
print(yesterday.strftime("%d%m%y"))
ystrday = str(yesterday.strftime("%d-%m-%Y"))
print(ystrday)
   
Download_page="http://www.srldc.in/var/ftp/reports/psp/2018/Mar18/15-03-2018-psp.pdf"

act_dwn_lnk= ("http://www.srldc.in/var/ftp/reports/psp/2018/Mar18/"+ystrday+"-psp.pdf")

urllib.request.urlretrieve(act_dwn_lnk, filename= "SRLDC"+ystrday+".pdf")


