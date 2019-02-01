
Created on Fri Mar 16 15:37:57 2018

@author: abhishek chandel

import urllib.request
import datetime
import urllib


#%y gives date in 2 digits and %Y gives data in 4 digits    
yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
print(yesterday.strftime("%d%m%y"))
ystrday = str(yesterday.strftime("%d%m%y"))
print(ystrday)
   
Download_page="https://nrldc.in/reports/daily-reports/daily-regional-power-supply-position/"

act_dwn_lnk= ("https://nrldc.in/Websitedata/DoReport/pdf/daily"+ystrday+".pdf")

urllib.request.urlretrieve(act_dwn_lnk, filename= "NRLDC"+ystrday+".pdf")
