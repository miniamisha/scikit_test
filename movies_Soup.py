#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 17:31:51 2017

@author: amisha
"""

import urllib2
link="https://archive.ics.uci.edu/ml/machine-learning-databases/movies-mld/data/main.html"
page=urllib2.urlopen(link)

from bs4 import BeautifulSoup
soup=BeautifulSoup(page)

print soup.prettify()

soup.title

soup.title.string

soup.a

right_table=soup.find_all('table', class_='linktable sortable plainrow')

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') 
    if len(cells)==6: 
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))
                
 import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['title']=B
df['year']=C
df['director']=D
df['Producer']=E
df['Award']=F
df['Notes']=G
df