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
        leccn = open(fncn, "w+")
        
        if "# Competitions" in lecenu:
            leccn.write(lecenu.replace("# Competitions", "# 竞赛"))
        elif "# Comprehensive Research" in lecenu:
            leccn.write(lecenu.replace("# Comprehensive Research", "# 综合性研究"))
        elif "# Economic, Urban planning and Govermance correlated resources" in lecenu:
            leccn.write(lecenu.replace("# Economic, Urban planning and Govermance correlated resources", "# 经济，城市规划与政府治理相关资源"))
        elif "# Funding application" in lecenu:
            leccn.write(lecenu.replace("# Funding application", "# 基金申请"))
        elif "# ISLE" in lecenu:
            leccn.write(lecenu.replace("# ISLE", "# 国际空间健康研究中心"))
        elif "# Journal special issues" in lecenu:
            leccn.write(lecenu.replace("# Journal special issues", "# 期刊特刊"))
        elif "# Lecture" in lecenu:
            leccn.write(lecenu.replace("# Lecture", "# 讲座与课程"))
        elif "# Organizations" in lecenu:
            leccn.write(lecenu.replace("# Organizations", "# 学术组织"))
        elif "# Sustainable cities & mobility" in lecenu:
            leccn.write(lecenu.replace("# Sustainable cities & mobility", "# 一览众山小-可持续城市与交通"))
        else:
            leccn.write(lecenu.replace("# Virology correlated Resources", "# 病毒学与生物学相关资源"))      
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
            leccn = open(fncn, "w+")
            if "# Journal" in lecenu:
                leccn.write(lecenu.replace("# Journal", "# 期刊"))
            elif "# University & Institute & Company" in lecenu:
                leccn.write(lecenu.replace("# University & Institute & Company", "# 大学 & 研究机构 & 公司"))
            elif "# WHO, CDC and other correlated department" in lecenu:
                leccn.write(lecenu.replace("# WHO, CDC and other correlated department", "# 世界卫生组织, 疾病预防控制中心与其他相关机构"))
            elif "# Academic paper letter" in lecenu:
                leccn.write(lecenu.replace("# Academic paper letter", "# 学术快报"))
            elif "# The News" in lecenu:
                leccn.write(lecenu.replace("# The News", "# 新闻"))
            elif "# Radiology" in lecenu:
                leccn.write(lecenu.replace("# Radiology", "# 影像学"))
            elif "# Clinic Medicine" in lecenu:
                leccn.write(lecenu.replace("# Clinic Medicine", "# 临床医学"))
            elif "# Modeling spearding and epidemiological analysis" in lecenu:
                leccn.write(lecenu.replace("# Modeling spearding and epidemiological analysis", "# 疫情传播建模与流行病学分析"))
            elif "# Risk assessment" in lecenu:
                leccn.write(lecenu.replace("# Risk assessment", "# 风险评估"))
            elif "# Evaluation intervention" in lecenu:
                leccn.write(lecenu.replace("# Evaluation intervention", "# 公共卫生干预评估"))
            elif "# Data" in lecenu:
                leccn.write(lecenu.replace("# Data", "# 数据"))
            elif "# Visualization" in lecenu:
                leccn.write(lecenu.replace("# Visualization", "# 可视化"))
            elif "# Platform(Including 3S Technology)" in lecenu:
                leccn.write(lecenu.replace("# Platform(Including 3S Technology)", "# 平台（包括3S技术）"))
            else:
                leccn.write(lecenu.replace("# Tools", "# 工具"))
    lecen.close()
    leccn.close()
