
from matplotlib import pyplot as plt

days= [0,1,2,3,4,5,6]
money_spent = [10,12,12,10,14,22,24]

plt.plot(days, money_spent)
plt.show ()


from matplotlib import pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot (time,revenue)
plt.plot (time, costs)

plt.show()


from matplotlib import pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot (time, costs, color='purple', linestyle=':')
plt.show()


from matplotlib import pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot (time, revenue, marker='o', color='purple', linestyle='--')
plt.plot (time, costs, marker='s', color='#82edc9')

plt.show()



from matplotlib import pyplot as plt

x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)

#your code here
plt.axis ([0,12,2900,3100])
plt.show()


#import codecademylib
from matplotlib import pyplot as plt

x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)
plt.axis([0, 12, 2900, 3100])
plt.xlabel ('Time')
plt.ylabel ('Dollars spent on coffee')
plt.title ('My Last Twelve Years of Coffee Drinking')

plt.show()

from matplotlib import pyplot as plt

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

plt.subplot(1,2,1)
plt.plot(months, temperature)

plt.subplot(1,2,2)
plt.plot(months, flights_to_hawaii)

plt.show()


from matplotlib import pyplot as plt
# 2 rows and 2 columns:
x = range(10)

# positive line in the first quadrant
plt.subplot(2, 2, 1)
plt.plot(x, [i for i in x])

# parabola in the second quadrant
plt.subplot(2, 2, 2)
plt.plot(x, [i**2 for i in x])

# negative line in the third quadrant
plt.subplot(2, 2, 3)
plt.plot(x, [-i for i in x])

# quartic in the fourth quadrant
plt.subplot(2, 2, 4)
plt.plot(x, [i**4 for i in x])

plt.show()


from matplotlib import pyplot as plt

x = range(7)
straight_line = [i for i in x]
parabola = [i**2 for i in x]
cubic = [i**3 for i in x]

plt.subplot(2,1,1)
plt.plot(x, straight_line, marker='s')

plt.subplot(2,2,3)
plt.plot(x, parabola)


plt.subplot(2,2,4)
plt.plot(x, cubic)

plt.subplots_adjust(wspace=0.35, bottom=0.1)

plt.show()


#import codecademylib
from matplotlib import pyplot as plt

months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)

#create your legend here

legend_labels = ["Hyrule", "Kakariko", "Gerudo Valley"]
plt.legend (legend_labels, loc=9)
#can also use legend = "" directly in the plt.plot method
#loc takes a value b/w 0 and 10 
plt.show()


#import codecademylib
#this example shows how to set specific axes and change them to strings
from matplotlib import pyplot as plt

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

plt.xlabel("Months")
plt.ylabel("Conversion")

plt.plot(months, conversion)

# Your work here
ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
ax.set_yticks([0.1, 0.25, 0.5, 0.75])
ax.set_yticklabels(["10%", "25%", "50%", "75%"])

plt.show()



"""
Figures
When we're making lots of plots, it's easy to end up with lines that have been plotted and not displayed. If we’re not careful, these "forgotten" lines will show up in your new plots. In order to be sure that you don't have any stray lines, you can use the command plt.close('all') to clear all existing plots before you plot a new one.

We can use the command plt.figure() to create new figures and size them how we want. We can add the keyword figsize and pass a tuple of (width, height) to set the size of the figure, in inches.

Note: Like plt.plot, plt.figure also creates a handle to the object. We also tend not to use it for anything, so we often don’t save it. Be aware that there are some advanced techniques that use it.
"""
#import codecademylib
from matplotlib import pyplot as plt

word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

plt.close('all')
plt.figure()
plt.plot(years, word_length)
plt.savefig('winning_word_lengths.png')


plt.figure(figsize=(7,3))
plt.plot(years, power_generated)
plt.savefig('power_generated.png')

plt.show()


#import codecademylib
from matplotlib import pyplot as plt

#x is years from 04-09 
x= [2004, 2005, 2006, 2007, 2008, 2009]

#y1 is government spending on science/tech
y1 = [23.029, 23.597, 23.584, 25.525, 27.731, 29.449]

#y2 is arcade revenue
y2 = [1.307, 1.435, 1.601, 1.654, 1.803, 1.734]

plt.plot(x, y1, color="pink", marker="o")
plt.plot(x, y2, color="gray", marker="o")
plt.title("Two Lines on One Graph")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")

legend_labels = ["Gov. Spending Sci/Tech", "Arcade Revenues"]
plt.legend(legend_labels, loc=7)

ax= plt.subplot()
plt.show()