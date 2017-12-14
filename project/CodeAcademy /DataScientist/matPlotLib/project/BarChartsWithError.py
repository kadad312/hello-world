#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 14:51:34 2017

@author: khaledadad
"""


from matplotlib import pyplot as plt

past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

# Make your chart here
plt.figure(figsize=(10,8))
plt.bar(range(len(years)), past_years_averages, yerr=error, capsize=5)
plt.axis([-0.5,6.5, 70, 95])
#for axis, numers are: [xmin, xmax, ymin, ymax]
plt.title("Final Exam Averages")
plt.ylabel("Test Average")
plt.xlabel("Year")
plt.savefig("my_bar_chart.png")
plt.show()
