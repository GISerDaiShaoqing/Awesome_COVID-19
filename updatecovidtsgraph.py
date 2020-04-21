# -*- coding: utf-8 -*-
#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import urllib
import json
import matplotlib as mpl
import datetime as dt
import time

def plot_covid():
    url = "https://coronavirus-tracker-api.herokuapp.com/v2/latest?source=jhu"
    apipage = urllib.request.urlopen(url)
    result = apipage.read()
    covidjson = json.loads(result)
    
    urlts = "https://covid19.mathdro.id/api/daily"
    
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

sched_time= dt.datetime(2020, 4, 22, 5, 0, 0)
timedelta=dt.timedelta(hours=1)

while True:
    nown=dt.datetime.now()
    nown=str(nown)[:-7]
    if nown==str(sched_time):
        print(nown)
        try:
            plot_covid()
        except:
            time.sleep(120)
            plot_covid()
    else:
        if nown==str(sched_time+timedelta):
            sched_time=sched_time+timedelta
            print(nown)
            try:
                plot_covid()
            except:
                time.sleep(120)
                plot_covid()
        else:
            pass