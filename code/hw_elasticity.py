# 
# HW-Elasticity (2013-04-25)
#
# Eungchan Kim  
#

from math import log, exp
from scipy.stats import linregress
import numpy as np
import csv

day_price = []
day_room = []
day_elasticity = 0
end_price = []
end_room = []
end_elasticity = 0

with open('price-elasticity.csv','r') as csvfile:
	line = csv.reader(csvfile, delimiter=',', quotechar='|')
	for i, value in enumerate(line):
		if i >0:
			if int(value[0]) < 6:
				day_room.append(log(float(value[1])))
				day_price.append(log(float(value[2][1:-1])))
			else: 
				end_room.append(log(float(value[1])))
				end_price.append(log(float(value[2][1:-1])))

droom = np.array(day_room)
dprice = np.array(day_price)
eroom = np.array(end_room)
eprice = np.array(end_price)

d_slope, d_intercept, d_r_value, d_p_value, d_std_err = linregress(droom, dprice)
e_slope, e_intercept, e_r_value, e_p_value, e_std_err = linregress(eroom, eprice)

print "Q1) The price elasticity of weekday : ", d_slope
print "Q2) The price elasticity of weekend : ", e_slope
print "\n"
print "Q3) The price for max revenue"

# According to the price elasticity I found above, 
# we can find the relationship between the change rate of the quantity of booked room
# and the change rate of price.
# Then, by modifing the change rate of price, we can calculate the quantity of booked room 
# at the changed price and total revenue.
# Pick the change rate of price that makes revenue maximum. 

print "--------------weekday------------------"
high_revenue = 0
price_at_high_revenue = 0
for delta_price in range(-300,300):
	delta_room = d_slope*delta_price               
	changed_room = 100*(100+delta_room)/100  
	changed_price = 200*(100+delta_price)/100
	revenue = changed_room * changed_price
	if high_revenue < revenue:
		high_revenue = revenue
		price_at_high_revenue = changed_price

print  '$',price_at_high_revenue, ' when the revenue is $',high_revenue

print "--------------weekday------------------"
high_revenue = 0
price_at_high_revenue = 0

for delta_price in range(-300,300):
	delta_room = e_slope*delta_price
	changed_room = 100*(100+delta_room)/100
	changed_price = 200*(100+delta_price)/100
	revenue = changed_room * changed_price
	if high_revenue < revenue:
		high_revenue = revenue
		price_at_high_revenue = changed_price

print  '$',price_at_high_revenue, ' when the revenue is $',high_revenue
