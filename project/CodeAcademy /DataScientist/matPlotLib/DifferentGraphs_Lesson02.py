#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 09:08:22 2017

@author: khaledadad
"""

###############################################################

#this is the first example of a simple bar chart
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len([drinks])), sales)

plt.show()


#second example w/labeled x-axis
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)

#create your ax object here
ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks, rotation=30)

plt.show()

###############################################################

#plotting multiple bars on the same graph
#use a function that takes inputs and calculates distances for bars
"""
To create plots with several sets of bars, we have to calculate x-values so that the bars line up.
 We can use the following formula to line them up:

[t*x + w*n for x in range(d)]
where:

n is the number of the series (in our population example, China is 1 and the United States is 2)
t is the total number of series to plot (in our population example, t is 2)
d is the number of data points (in our population example, d is 7 because we plotted 7 separate years)
w is the width of each bar (we will mostly use the default of 0.8)
"""

from matplotlib import pyplot as plt

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
  
# Use create_x to make store1_x
store1_x = create_x(2,0.8,1,6)
plt.bar(store1_x, sales1)
# Use create_x to make store2_x
store2_x = create_x(2,0.8,2,6)
plt.bar(store2_x, sales2)

plt.show()

###############################################################
"""
Stacked Bars
If we want to compare two sets of data while preserving knowledge of the total between them, 
we can also stack the bars instead of putting them side by side. 
For instance, if someone was plotting the hours they've spent on entertaining themselves with video games and books in the past week, 
and wanted to also get a feel for total hours spent on entertainment, they could create a stacked bar chart.

We do this by using the keyword bottom. The top set of bars will have bottom set to the heights of the other set of bars. So the first set of bars is plotted normally:

video_game_hours = [1, 2, 2, 1, 2]

plt.bar(range(len(video_game_hours)),
  video_game_hours)
and the second set of bars has bottom specified:

book_hours = [2, 3, 4, 2, 1]

plt.bar(range(len(book_hours)),
  book_hours,
  bottom=video_game_hours)
This starts the book_hours bars at the heights of the video_game_hours bars. So, for example, on Monday the orange bar representing hours spent reading will start at a value of 1 instead of 0, because 1 hour was spent playing video games.
"""

from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

plt.bar(range(len(drinks)), sales1)
plt.bar(range(len(drinks)), sales2, bottom=sales1)

legend_labels = ['Location 1','Location 2']
plt.legend(legend_labels, loc=9)
plt.xlabel('Days')
plt.ylabel('Store Sales')

plt.show()

###############################################################
"""
Error Bars
In the previous exercise, you learned to represent data as bars of different heights. Sometimes, we need to visually communicate some sort of uncertainty in the heights of those bars. Here are some examples:

The average number of students in a 3rd grade classroom is 30, but some classes have as few as 18 and others have as many as 35 students.
We measured that the weight of a certain fruit was 35g, but we know that our scale isn’t very precise, so the true weight of the fruit might be as much as 40g or as little as 30g.
The average price of a soda is $1.00, but we also want to communicate that the standard deviation is $0.20.
To display error visually in a bar chart, we often use error bars to show where each bar could be, taking errors into account. To create error bars in a Matplotlib chart, we use yerr. The convention is also to have "caps", or little horizontal lines at the top and bottom of the error bar. To make these, we use the keyword capsize with a non-zero number. The bigger the number, the longer the caps are.

Here is an example of how to call plt.bar with the keywords yerr and capsize:

values = [10, 13, 11, 15, 20]
yerr = 2
plt.bar(range(len(values)), values, yerr=yerr, capsize=10)
plt.show()

We can also pass in list of numbers, if the error on each measurement is different:

values = [10, 13, 11, 15, 20]
yerr = [1, 3, 0.5, 2, 4]
plt.bar(range(len(values)), values, yerr=yerr, capsize=10)
plt.show()
This code results in error bars of different sizes.
"""

from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.1*e for e in ounces_of_milk]
#According to different barista styles and measurement errors, there might be variation on how much milk actually goes into each drink. 
#We've included a list error, with an error of 10% on each amount of milk. Display this error as error bars on the bar graph.

# Plot the bar graph here
plt.bar(range(len(drinks)), ounces_of_milk, yerr=error, capsize=5)

plt.show()

###############################################################
"""
Fill Between
We’ve learned how to display errors on bar charts using error bars. Let’s take a look at how we might do this in an aesthetically pleasing way on line graphs. In Matplotlib, we can use plt.fill_between to shade error. This function takes three arguments:

x-values — this works just like the x-values of plt.plot
lower-bound for y-values — sets the bottom of the shared area
upper-bound for y-values — sets the top of the shared area
Generally, we use fill_between to create a shaded error region, and then plot the actual line over it. We can set the alpha keyword to a value between 0 and 1 in the fill_between call for transparency so that we can see the line underneath. Here is an example of how we would display data with an error of 2:

from matplotlib import pyplot as plt

x_values = range(10)
y_values = [10, 12, 13, 13, 15, 19, 20, 22, 23, 29]
error = 2
y_lower = [i - error for i in y_values]
y_upper = [i + error for i in y_values]

plt.fill_between(x_values, y_lower, y_upper, alpha=0.2) #this is the shaded error
plt.plot(x_values, y_values) #this is the line itself
plt.show()
"""
from matplotlib import pyplot as plt

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

#your work here
y_lower=[i-i*.1 for i in revenue] 
y_upper= [i+i*.1 for i in revenue]
#standard error here is 10% on top and 10% on the bottom
"""You could create y_lower using a list comprehension [i - (i*decimal_of_error) for i in y], which would subtract i*decimal_of_error from each element i in the list revenue.

Or you could calculate i minus 10% of i by hand for each element i in the list revenue.

For example, the first element in revenue is 16000, so the first element in y_lower is:

16000 - 16000*0.1
or 14400."""

plt.fill_between(months,y_lower,y_upper,alpha=.2)

x = range(12)
plt.plot(x, revenue)

ax=plt.subplot()
ax.set_xticks(x)
ax.set_xticklabels(month_names, rotation=30)

plt.show()

###############################################################
"""
Pie Chart
If we want to display elements of a data set as proportions of a whole, we can use a pie chart.

Pie charts are helpful for displaying data like:

Different ethnicities that make up a school district
Different macronutrients (carbohydrates, fat, protein) that make up a meal
Different responses to an online poll
In Matplotlib, you can make a pie chart with the command plt.pie, passing in the values you want to chart:

budget_data = [500, 1000, 750, 300, 100]

plt.pie(budget_data)
plt.show()

This looks weird and tilted. 
When we make pie charts in Matplotlib, we almost always want to set the axes to be equal to fix this issue. 
To do this, we use plt.axis('equal')

budget_data = [500, 1000, 750, 300, 100]
plt.axis('equal')
plt.pie(budget_data)
plt.show()

"""

from matplotlib import pyplot as plt
import numpy as np

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

#make your pie chart here
plt.axis('equal')
plt.pie(payment_method_freqs)

plt.show()

###############################################################
"""
Pie Chart Labeling
We also want to be able to understand what each slice of the pie represents. To do this, we can either:

use a legend to label each color, or
put labels on the chart itself.

METHOD 1

budget_data = [500, 1000, 750, 300, 100]
budget_categories = ['marketing', 'payroll', 'engineering', 'design', 'misc']

plt.legend(budget_categories)
plt.pie(budget_data)
This puts the category names into a legend on the chart

METHOD 2

plt.pie(budget_data, labels=budget_categories)
This puts the category names into labels next to each corresponding slice.

One other useful labeling tool for pie charts is adding the percentage of the total that each slice occupies.
 Matplotlib can add this automatically with the keyword autopct. 
 We pass in string formatting instructions to format the labels how we want.
 Some common formats are:

'%0.2f' — 2 decimal places, like 4.08
'%0.2f%%' — 2 decimal places, but with a percent sign at the end, like 4.08%. 
You need two consecutive percent signs because the first one acts as an escape character, so that the second one gets displayed on the chart.
'%d%%' — rounded to the nearest int and with a percent sign at the end, like 4%.
So, a full call to plt.pie might look like:

plt.pie(budget_data,
        labels=budget_categories,
        autopct='%0.1f%%')

"""


from matplotlib import pyplot as plt

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.pie(payment_method_freqs, autopct='%0.1f%%')
plt.axis('equal')
plt.legend(payment_method_names)

plt.show()

###############################################################
"""
Histogram
Sometimes we want to get a feel for a large dataset with many samples beyond knowing just the basic metrics of mean, median, or standard deviation.
 To get more of an intuitive sense for a dataset, we can use a histogram to display all the values. 
 Histograms are best for showing the shape of a dataset. 
 For example, you might see that values are close together, or skewed to one side. 
 With this added intuition, we often discover other types of analysis we want to perform.
 
To make a histogram in Matplotlib, we use the command plt.hist. plt.hist finds the minimum and the maximum values in your dataset and creates equally-spaced "bins" between those values. It counts how many values from the dataset fall into each bin, and those counts become the height of each bar.

The histogram above, for example, was created with the following code:

from numpy.random import normal
gaussianDist = normal(loc=68, scale=2, size=10000)

plt.hist(gaussianDist) 
plt.show()

It also returns values with the boundaries and heights of each bin, but we often don’t do anything with these.

We can use the keyword bins to set how many bins we want to divide the data into. 
By default, this is set to 10. The keyword range selects the minimum and maximum values to plot. 
For example, if we wanted to take our Gaussian from the last example and make a new histogram that just displayed the values from 66 to 69, divided into 40 bins (instead of 10), we could use this function call:


plt.hist(a, range=(66,69), bins=40)
    
"""
"""

KHALED KHALED KHALED
I COMMENTED THIS SECTION OUT BECAUSE IT IS IMPORTING A FUNCTION
THAT IMPORTS THE CSV FILE THAT I HAVE SAVED ALONGSIDE THIS PYTHON
TUTORIAL
BELOW IS THE PYTHON CODE TO IMPORT THE DATA AND CONVERT IT FROM THE .CSV 
FORMAT THAT IS SAVED IN THE SAME FOLDER

BELOW THAT IS THE PYTHON CODE TO CREATE A SIMPLE HISTOGRAM BASED OFF OF THE DATA


from matplotlib import pyplot as plt
import csv

def convert_time_to_num(time):
  mins = int(time[-2:])
  frac_of_hour = mins/60.0
  hour = int(time[:-3])
  time = hour + frac_of_hour
  return time

sales_times_raw = []
with open('sales_times.csv') as csvDataFile:
  csvReader = csv.reader(csvDataFile)
  for row in csvReader:
    sales_times_raw.append(row[2])
  sales_times_raw = sales_times_raw[1:]

sales_times = []
for time in sales_times_raw:
  sales_times.append(convert_time_to_num(time))
  
"""

###
from matplotlib import pyplot as plt
from script import sales_times

#create the histogram here
plt.hist(sales_times, bins=20)
plt.show()

###############################################################
"""
Multiple Histograms
If we want to compare two different distributions, we can put multiple histograms on the same plot. 
This could be useful, for example, in comparing the heights of a bunch of men and the heights of a bunch of women.
 However, it can be hard to read two histograms on top of each other. 
 
 We have two ways we can solve a problem like this:

1. use the keyword alpha, which can be a value between 0 and 1. 

This sets the transparency of the histogram. 
A value of 0 would make the bars entirely transparent. 
A value of 1 would make the bars completely opaque.

from matplotlib import pyplot as plt
a = normal(loc=64, scale=2, size=10000)
b = normal(loc=70, scale=2, size=10000)

plt.hist(a, range=(55, 75), bins=20, alpha=0.5)
plt.hist(b, range=(55, 75), bins=20, alpha=0.5)

This would make both histograms visible on the plot.

2. use the keyword histtype with the argument 'step' to draw just 
the outline of a histogram:

plt.hist(a, range=(55, 75), bins=20, histtype='step')
plt.hist(b, range=(55, 75), bins=20, histtype='step')

Another problem we face is that our histograms might have different 
numbers of samples, making one much bigger than the other. 
We can see how this makes it difficult to compare qualitatively, 
by adding a dataset b with a much bigger size value:

from matplotlib import pyplot as plt

a = normal(loc=64, scale=2, size=10000)
b = normal(loc=70, scale=2, size=100000)

plt.hist(a, range=(55, 75), bins=20)
plt.hist(b, range=(55, 75), bins=20)
plt.show()
The result is two histograms that are very difficult to compare

To solve this, we can normalize our histograms using normed=True.
 This command divides the height of each column by a constant such that 
 the area under the curve sums to 1.

from matplotlib import pyplot as plt

a = normal(loc=64, scale=2, size=10000)
b = normal(loc=70, scale=2, size=100000)

plt.hist(a, range=(55, 75), bins=20, alpha=0.5, normed=True)
plt.hist(b, range=(55, 75), bins=20, alpha=0.5, normed=True)
plt.show()

"""
#note this bottom exercise with two histograms doesn't work b/c it can't see
#the .csv file that another python file is pointing to

from matplotlib import pyplot as plt
from script import sales_times1
from script import sales_times2

plt.hist(sales_times1, bins=20, alpha=0.4, normed=True)
plt.hist(sales_times2, bins=20, alpha=0.4, normed=True)
#plot your other histogram here

plt.show()







