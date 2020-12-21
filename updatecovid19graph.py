# -*- coding: utf-8 -*-
#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import urllib
import json
import matplotlib as mpl
import datetime as dt
import time

def plot_covid(url, urlts):
    apipage = urllib.request.urlopen(url)
    result = apipage.read()
    covidjson = json.loads(result)
      
    apipagets = urllib.request.urlopen(urlts)
    resultts = apipagets.read()
    covidjsonts = json.loads(resultts)
    
    datelist = []
    clist = []
    dlist = []
    
    for i in range(0, len(covidjsonts), 1):
        datelist.append(covidjsonts[i]['reportDate'])
        clist.append(covidjsonts[i]['totalConfirmed'])
        dlist.append(covidjsonts[i]['deaths']['total'])
        
    coviduts = {'Date': datelist, 
                'Confirmed': clist, 
                'Death': dlist}
    covidfts = pd.DataFrame(coviduts)
    
    today = dt.datetime.now() 
    today
    
    time = today.strftime("%Y-%m-%d %H:%M:%S")
    today = today.strftime("%Y-%m-%d")
    
    confirmedtext = 'Total Confirmed Cases: ' + str(covidjson['latest']['confirmed'])
    deathtext = 'Total Death Cases: ' + str(covidjson['latest']['deaths'])
    cfrtext = 'Mortality rate/%: ' + str(round(covidjson['latest']['deaths']/covidjson['latest']['confirmed']*100, 3))
    updatext = 'Last Updated at: ' + str(time) + '(Beijing Time)'
    
    plt.figure(figsize=(20, 12))
    plt.title('The curve of COVID-19', fontsize=30) 
    plt.plot(covidfts['Date'], covidfts['Confirmed'], color ='yellow', label = 'Confirmed Cases')
    plt.plot(covidfts['Date'], covidfts['Death'], color = 'blue',  label = 'Death Cases')
    plt.xticks(rotation=-90)
    plt.legend()
    plt.text('2020-01-25', 0.75*covidfts['Confirmed'].max(), confirmedtext, fontsize=20)
    plt.text('2020-01-25', 0.6*covidfts['Confirmed'].max(), deathtext, fontsize=20)
    plt.text('2020-01-25', 0.45*covidfts['Confirmed'].max(), cfrtext, fontsize=20)
    plt.text('2020-01-25', 0.3*covidfts['Confirmed'].max(), updatext, fontsize=20)
    plt.xlabel('Date', fontsize=20)
    plt.ylabel('Persons', fontsize=20)
    plt.savefig('website/img/architecture.png', dpi = 300)

def plot_jhuraw():
    #covidc = pd.read_csv("https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
    #covidd = pd.read_csv("https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
    covidc = pd.read_csv("/home/PhDITC/COVID19web/website/coviddatacon.csv")
    covidd = pd.read_csv("/home/PhDITC/COVID19web/website/coviddatadea.csv")
    
    covidc['World'] = "Worldwide"
    covidd['World'] = "Worldwide"
    
    covidcts = covidc.groupby('World').sum()
    covidcpdf = pd.DataFrame(covidcts.ix[0][2:])
    
    coviddts = covidd.groupby('World').sum()
    coviddpdf = pd.DataFrame(coviddts.ix[0][2:])
    
    covidcpdf = covidcpdf.reset_index()
    coviddpdf = coviddpdf.reset_index()
    
    today = dt.datetime.now() 
    today
    
    time = today.strftime("%Y-%m-%d %H:%M:%S")
    today = today.strftime("%Y-%m-%d")
    
    confirmedtext = 'Total Confirmed Cases: ' + str(list(covidcpdf.Worldwide)[-1])
    deathtext = 'Total Death Cases: ' + str(list(coviddpdf.Worldwide)[-1])
    cfrtext = 'Mortality rate/%: ' + str(round(list(coviddpdf.Worldwide)[-1]/list(covidcpdf.Worldwide)[-1]*100, 3))
    updatext = 'Last Updated at: ' + str(time) + '(Beijing Time)'
    
    plt.figure(figsize=(20, 12))
    plt.title('The curve of COVID-19', fontsize=30) 
    plt.plot(covidcpdf['index'], covidcpdf['Worldwide'], color ='yellow', label = 'Confirmed Cases')
    plt.plot(coviddpdf['index'], coviddpdf['Worldwide'], color = 'blue',  label = 'Death Cases')
    plt.xticks(rotation=-90)
    plt.legend()
    plt.text(covidcpdf['index'][2], 0.75*covidcpdf['Worldwide'].max(), confirmedtext, fontsize=20)
    plt.text(covidcpdf['index'][2], 0.6*covidcpdf['Worldwide'].max(), deathtext, fontsize=20)
    plt.text(covidcpdf['index'][2], 0.45*covidcpdf['Worldwide'].max(), cfrtext, fontsize=20)
    plt.text(covidcpdf['index'][2], 0.3*covidcpdf['Worldwide'].max(), updatext, fontsize=20)
    plt.xlabel('Date', fontsize=20)
    plt.ylabel('Persons', fontsize=20)
    plt.savefig('/home/PhDITC/COVID19web/website/img/architecture.png', dpi = 300)


plot_jhuraw()