# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 16:37:20 2018

@author: abhishek chandel
"""




import urllib.request
import datetime
import urllib


#%y gives date in 2 digits and %Y gives data in 4 digits    
today = datetime.datetime.now()
print(today.strftime("%d%m%y"))
today = str(today.strftime("%d%m%y"))
print(today)
   
Download_page="http://www.nerldc.org/DR/DR160318.pdf"

act_dwn_lnk= ("http://www.nerldc.org/DR/DR"+today+".pdf")

urllib.request.urlretrieve(act_dwn_lnk, filename= "NERLDC"+today+".pdf")