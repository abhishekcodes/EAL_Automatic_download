# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 12:42:07 2018

@author: abhishek chandel
"""

from bs4 import BeautifulSoup as BS
import urllib.request
import datetime
import urllib
import tabula

#to import it into excel csv using
import csv


today = datetime.datetime.now()
today = str(today.strftime("%d%m%y"))
print(today)
yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
ystrday = str(yesterday.strftime("%d%m%y"))
 
def Download_NLDC_file_daily():
    Date = datetime.datetime.now().strftime("%d-%m-%y")
    Date = str(Date)
    print(Date)
    #this step give the link of webpage b y which we will import the html text to parse
    Download_page_sample_NLDC='https://posoco.in/reports/daily-reports/daily-reports-2017-18'
    #this step is to open the webpage and reading is done and it is saved in the variable named page
    page= urllib.request.urlopen(Download_page_sample_NLDC).read()
    #this step will parse the data using BS4 module
    prossd_page= BS(page, 'lxml')
    #now we will find all a tags inside the parsed data
    dwnld_links = prossd_page.findAll("a", href= True)
    #this step will give the info within first cell of table
    dwnld_link_td = prossd_page.td.a
    #this will convert the bs4.Resultelement into str
    dwnld_str= str(dwnld_link_td)
    #this will split the string further to get groups of strings seperated by white spaces
    element= dwnld_str.split()
    #this will pick up the first element of the element list generated above
    dwn_lnk= str(element[1])
    #this will precisely pick the dynamic download link
    act_dwn_lnk= dwn_lnk[6:64]
    #this function will download the file form the text generated from the scraping 
    urllib.request.urlretrieve(act_dwn_lnk, filename= "NLDC"+Date+".pdf")


def Download_NRLDC_file_daily():
    yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
    ystrday = str(yesterday.strftime("%d%m%y"))
    print(ystrday)
    Download_page_sample_NRLDC="https://nrldc.in/reports/daily-reports/daily-regional-power-supply-position/"
    act_dwn_lnk= ("https://nrldc.in/Websitedata/DoReport/pdf/daily"+ystrday+".pdf")
    urllib.request.urlretrieve(act_dwn_lnk, filename= "NRLDC"+ystrday+".pdf")


def Download_WRLDC_file_daily():
    today = datetime.datetime.now()
    print(today.strftime("%d%m%y"))
    today = str(today.strftime("%d%m%Y"))
    print(today)
    Download_page_sample_WRLDC="http://www.wrldc.in/9_reportNew/dailydata_13032018.pdf"
    act_dwn_lnk= ("http://www.wrldc.in/9_reportNew/dailydata_"+today+".pdf")
    urllib.request.urlretrieve(act_dwn_lnk, filename= "WRLDC"+today+".pdf")

def Download_SRLDC_file_daily():
    yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
    print(yesterday.strftime("%d%m%y"))
    ystrday = str(yesterday.strftime("%d-%m-%Y"))
    print(ystrday)
    Download_page_sample_SRLDC="http://www.srldc.in/var/ftp/reports/psp/2018/Mar18/15-03-2018-psp.pdf"
    act_dwn_lnk= ("http://www.srldc.in/var/ftp/reports/psp/2018/Mar18/"+ystrday+"-psp.pdf")
    urllib.request.urlretrieve(act_dwn_lnk, filename= "SRLDC"+ystrday+".pdf")

def Download_NERLDC_file_daily():
    yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
    print(yesterday.strftime("%d%m%y"))
    ystrday = str(yesterday.strftime("%d%m%y"))
    print(ystrday)
    Download_page_sample_NERLDC="http://www.nerldc.org/DR/DR160318.pdf"
    act_dwn_lnk= ("http://www.nerldc.org/DR/DR"+ystrday+".pdf")
    urllib.request.urlretrieve(act_dwn_lnk, filename= "NERLDC"+ystrday+".pdf")
    
def Download_ERLDC_file_daily():
    yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
    print(yesterday.strftime("%d%m%y"))
    ystrday = str(yesterday.strftime("%d%m%Y"))
    print(ystrday)
    act_dwn_lnk= (r"https://app.erldc.in/Content/Upload/Report/PSP/PSP_Report_"+ystrday+".pdf")
    urllib.request.urlretrieve(act_dwn_lnk, filename= "ERLDC"+ystrday+".pdf")
    

def Download_files():
    Download_NLDC_file_daily()
    Download_NRLDC_file_daily()
    Download_WRLDC_file_daily()
    Download_SRLDC_file_daily()
    Download_NERLDC_file_daily()
    Download_ERLDC_FILE_daily()


Download_files()


def convert_NLDC():
    df =tabula.read_pdf("NLDC"+today+".pdf", encoding="cp932",pages="all", multiple_tables=True,lattice =True)
    tabula.convert_into("NLDC"+today+".pdf", "NLDC"+today+".csv",output_format ="csv", multiple_tables= True,lattice= True,pages ="all")
    Regional_data = pd.DataFrame(df[0])
    FREQ = pd.DataFrame(df[1])
    PSPS = pd.DataFrame(df[2])
    ICTE = pd.DataFrame(df[3])
    IER =  pd.DataFrame(df[4])
    GEN_OUT = pd.DataFrame(df[5])
    SOURCE_GEN = pd.DataFrame(df[6])
    IRE = pd.DataFrame(df[7])
    
def convert_NRLDC():
    df =tabula.read_pdf("NRLDC"+ystrday+".pdf", encoding="cp932",pages="all", multiple_tables=True,lattice = True)
    tabula.convert_into("NRLDC"+ystrday+".pdf", "NRLDC"+ystrday+".csv",output_format ="csv", multiple_tables= True,lattice= True,pages ="all")
    R_A_D = pd.DataFrame(df[0])
    S_L_D = pd.DataFrame(df[1])
    S_D_M = pd.DataFrame(df[2])
    REG_ENT = pd.DataFrame(df[3])
    State_ENT =  pd.DataFrame(df[4])
    State_ENT_2 = pd.DataFrame(df[5])
    T_Hydro_GEN = pd.DataFrame(df[6])
    T_Ren_GEN = pd.DataFrame(df[7])
    IRE = pd.DataFrame(df[8])
    IR_S_ACT_EX = pd.DataFrame(df[9])
    IR_Analysis = pd.DataFrame(df[10])
    IRE_Nepal = pd.DataFrame(df[11])
    FREQ_Profile = pd.DataFrame(df[12])
    FREQ_Profile_3 = pd.DataFrame(df[13])
    VOL_Profile_400kV = pd.DataFrame(df[14])
    VOL_Profile_765kV = pd.DataFrame(df[15])
    Res_parameters = pd.DataFrame(df[16])
    STOA = pd.DataFrame(df[17])
    STOA_2 = pd.DataFrame(df[18])
    Sys_Rel_Indics = pd.DataFrame(df[19])
    Sys_Rel_Indics_2 = pd.DataFrame(df[20])
    Z_C_violations = pd.DataFrame(df[21])
    
    
def convert_WRLDC():
    today = datetime.datetime.now()
    today = str(today.strftime("%d%m%Y"))
    print(today)
    df =tabula.read_pdf("WRLDC"+today+".pdf", encoding="cp932",pages="all", multiple_tables=True,lattice= True)
    tabula.convert_into("WRLDC"+today+".pdf", "WRLDC"+today+".csv",output_format ="csv", multiple_tables= True,lattice= True,pages ="all")
    REQ_WR = pd.Dataframe(df[0])
    FREQ = pd.DataFrame(df[1])
    G_D_S_in_CA = pd.DataFrame(df[2])
    S_D_M = pd.DataFrame(df[3])
    REG =  pd.DataFrame(df[4])
    REG_IPP = pd.DataFrame(df[5])
    REG_IPP_2= pd.DataFrame(df[6])
    IRE = pd.DataFrame(df[7])
    VOL_Profile_765kV = pd.DataFrame(df[8])
    VOL_Profile_400kV = pd.DataFrame(df[9])
    STOA_BI_PX = pd.DataFrame(df[10])
    State_Genrtrs = pd.DataFrame(df[11])
    State_Genrtrs_2 = pd.DataFrame(df[12])
    Z_C_UI_S = pd.DataFrame(df[13])
    
def convert_SRLDC():
    yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
    print(yesterday.strftime("%d%m%y"))
    ystrday = str(yesterday.strftime("%d-%m-%Y"))
    print(ystrday)
    df =tabula.read_pdf("SRLDC"+ystrday+".pdf", encoding="cp932",pages="all", multiple_tables=True,lattice = True)
    tabula.convert_into("SRLDC"+ystrday+".pdf", "SRLDC"+ystrday+".csv",output_format ="csv", multiple_tables= True,lattice= True,pages ="all")
    REG_AV = pd.DataFrame(df[0])
    State_Demand = pd.DataFrame(df[1])
    S_D_Energy_Forecast = pd.DataFrame(df[2])
    GEN = pd.DataFrame(df[3])
    GEN_2 = pd.DataFrame(df[4])
    GEN_3 = pd.DataFrame(df[5])
    GEN_4 = pd.DataFrame(df[6])
    IRE_HVDC_Physical_Flows= pd.DataFrame(df[7])
    IRE_SCH_WHELNG_UI_TLCHR = pd.DataFrame(df[8])
    FREQ_Profile = pd.DataFrame(df[9])
    VOL_Critical_Sub_Station = pd.DataFrame(df[10])
    Maj_Res_Particulars = pd.DataFrame(df[11])
    Overdrawls_below_49HZ_Constituents= pd.DataFrame(df[12])
    Overdrawls_below_49HZ_Generators= pd.DataFrame(df[13])

def convert_NERLDC():
     df =tabula.read_pdf("NERLDC"+ystrday+".pdf", encoding="cp932",pages="all", multiple_tables=True,lattice = True)
     tabula.convert_into("NERLDC"+ystrday+".pdf", "NERLDC"+ystrday+".csv",output_format ="csv", multiple_tables= True,lattice= True,pages ="all")
     REG_AV= pd.DataFrame(df[0])
     
     
     
def convert_ERLDC():
    yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
    ystrday = str(yesterday.strftime("%d%m%Y"))
    df =tabula.read_pdf("ERLDC"+ystrday+".pdf", encoding="cp932",pages="all", multiple_tables=True,lattice = True)
    
     
     
     
     
def Convert_into_DataFrames():
    convert_NLDC()
    convert_NRLDC()
    convert_WRLDC()
    convert_SRLDC()
    convert_NERLDC()
    convert_ERLDC()
    
    
Convert_into_DataFrames()




















