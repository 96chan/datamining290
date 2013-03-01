#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""
from collections import defaultdict
import fileinput
import csv

column_name = 2  # Candidate Name
column_zip = 6  # Zipcode

############### Set up variables
# TODO: declare datastructures
cand_nm =defaultdict(int)
zip_each_total =defaultdict(int)
cand_nm_zip=defaultdict(list)

############### Read through files
for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
		cand_nm[row[column_name ]] +=1
		zip_each_total[row[column_zip]] +=1
		cand_nm_zip[row[column_zip]].append(row[column_name])

gini = 0  # current Gini Index using candidate name as the class
split_gini = 0  # weighted average of the Gini Indexes using candidate names, split up by zip code
total = 0

###
#simple gini
###
each_num = [] # count of each candidate
sum_frac = 0
#get total number and count of each candidate
for value in cand_nm:
	total += cand_nm[value]
	each_num.append(cand_nm[value])
for value in each_num:
	sum_frac = sum_frac + (value/float(total))**2
gini = 1-sum_frac

###
#weighted gini by zipcode
###
for zip in cand_nm_zip:
	# Initialize variables
	sum_sub_frac = 0
	sub_gini = 0
	num_cand_by_zip = defaultdict(int) # count the number of each candidate

	for names in cand_nm_zip[zip]: # cand_nm_zip[zip] list the candidate names according to the zipcode
		num_cand_by_zip[names] +=1 
	for cand_names in num_cand_by_zip: # calculate sum of sub_fraction
		sum_sub_frac += (num_cand_by_zip[cand_names]/float(zip_each_total[zip]))**2
	sub_gini = 1-sum_sub_frac # calculate sub gini per each zipcode
	split_gini += sub_gini* (zip_each_total[zip]/float(total)) # weighted average

print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini
