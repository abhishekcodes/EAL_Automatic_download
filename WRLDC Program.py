# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 16:17:07 2018

@author: abhishek chandel
"""

import urllib.request
import datetime
import urllib


#%y gives date in 2 digits and %Y gives data in 4 digits    
today = datetime.datetime.now()
print(today.strftime("%d%m%y"))
today = str(today.strftime("%d%m%Y"))
print(today)
   
Download_page="http://www.wrldc.in/9_reportNew/dailydata_13032018.pdf"

act_dwn_lnk= ("http://www.wrldc.in/9_reportNew/dailydata_"+today+".pdf")

urllib.request.urlretrieve(act_dwn_lnk, filename= "WRLDC"+today+".pdf")



http://www.srldc.in/var/ftp/reports/psp/2018/Mar18/15-03-2018-psp.pdf