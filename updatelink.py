# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:44:45 2020

@author: GIS-Watcher
"""

import os

path = "F:/PhDITC/COVID_19/Awesome_COVID-19/docs/en-us"
lists = os.listdir(path)

for i in range(0, len(lists), 1):
    fn = path + "/" + lists[i]
    if ".md" in fn:
        lecen = open(fn)
        lecenu = lecen.read()
        lecenline = lecenu.split("\n")
        
        fncn = fn.replace("en-us", "zh-cn")
        leccn = open(fncn)
        leccnu = leccn.read()
        leccnline = leccnu.split("\n")
        
        if len(lecenline)==len(leccnline):
            print("No update")
        else:
            print("Need to update")
            addlink = "\n"
            addn = len(lecenline) - len(leccnline)
            for k in range(0, len(lecenline[-addn:]), 1):
                addlink = addlink + lecenline[-addn:][k] + "\n"
            with open('zh/lec.md','a+') as f:
                f.write(addlink)
    elif "img" in fn:
        print("it's picture")         
    else:
        print("path")
        listsn = os.listdir(fn)
        for j in range(0, len(listsn), 1):
            fns = fn + "/" + listsn[j]
            lecen = open(fns)
            lecenu = lecen.read()
            lecenline = lecenu.split("\n")
        
            fncn = fns.replace("en-us", "zh-cn")
            leccn = open(fncn)
            leccnu = leccn.read()
            leccnline = leccnu.split("\n")
            if len(lecenline)==len(leccnline):
                print("No update")
            else:
                print("Need to update")
                addlink = "\n"
                addn = len(lecenline) - len(leccnline)
                for k in range(0, len(lecenline[-addn:]), 1):
                    addlink = addlink + lecenline[-addn:][k] + "\n"
                with open('zh/lec.md','a+') as f:
                    f.write(addlink)
