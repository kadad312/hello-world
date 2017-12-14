#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 15:13:13 2017

@author: khaledadad
"""


from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]
school_a_x = [0.8, 2.8, 4.8, 6.8, 8.8]
school_b_x = [1.6, 3.6, 5.6, 7.6, 9.6]
# Make your chart here
plt.figure(figsize=(10,8))
ax = plt.subplot()

plt.bar(school_a_x, middle_school_a)
plt.bar(school_b_x, middle_school_b)


"""
Create a new list of x-values called middle_x, which are the values in the middle of school_a_x and school_b_x. This is where we will place the x-ticks. Look at the final graph to see this placement.

Use list comprehension and zip to create middle_x:

middle_x = [ (a + b) / 2.0 for a, b in zip(school_a_x, school_b_x)]

"""
middle_x = [ (a + b) / 2.0 for a, b in zip(school_a_x, school_b_x)]

ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)

plt.axis([0,10,70,90])
legend_labels=['Middle School A','Middle School B']
plt.legend(legend_labels, loc=0)
plt.title('Test Averages on Different Units')
plt.xlabel('Unit')
plt.ylabel('Test Average')

plt.savefig('my_side_by_side.png')

plt.show()