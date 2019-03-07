#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 01:32:48 2019

"""
import matplotlib.pyplot as plt

x=[1,10,20,30,40]
y=[[0.012262, 0.0124742, 0.0124563,0.0115957,0.0123799],[0.012262, 0.0233148, 0.0186742, 0.0372553, 0.0866177],[0.012262, 0.0233148, 0.0186742, 0.0392493, 0.0886251]]
labels=['RR', 'PF', 'TDMT']
colors=['r','g','b']

# loop over data, labels and colors
for i in range(len(y)):
    plt.plot(x,y[i],'o-',color=colors[i],label=labels[i])

plt.legend()
plt.xlabel('no. of UEs')
plt.ylabel('UL latency')
plt.savefig('testplot.png')
