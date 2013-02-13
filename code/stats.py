#!/usr/bin/python
"""This script can be used to analyze data in the 2012 Presidential Campaign,
available from http://www.fec.gov/disclosurep/PDownload.do"""

import fileinput
import csv

total = 0
conb_amt_array = []
cand_nm_array = []

for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
        total += float(row[9])
        conb_amt_array.append(float(row[9]))
        cand_nm_array.append(row[2])

# TODO: aggregate any stored numbers here
def get_mean(s):
    return sum(s)/len(s)

def get_median(s):
    i=len(s)
    s= sorted(s)
    if not i%2:
        return (s[(i/2)-1]+s[i/2])/2.0
    return s[i/2]

def get_std(s):
    var =[]
    mean = get_mean(s) 
    variance = map(lambda x:(x - mean)**2, s)
    return get_mean(variance)**0.5

def get_candidate(s):
    return list(set(s)) 

min_ = min(conb_amt_array)
max_ = max(conb_amt_array)

##### Print out the stats
print "Total: %s" % total
print "Minimum:%s" % min_
print "Maximum:%s" % max_
print "Mean: %s" % get_mean(conb_amt_array) 
print "Median: %s" % get_median(conb_amt_array)
# square root can be calculated with N**0.5
print "Standard Deviation:%s " % get_std(conb_amt_array)

##### Comma separated list of unique candidate names
print "Candidates:%s " % get_candidate(cand_nm_array)

def minmax_normalize(value):
    """Takes a donation amount and returns a normalized value between 0-1. The
    normilzation should use the min and max amounts from the full dataset"""
    norm = 0+(1-0)*(value-min_)/(max_-min_) 
    return norm

##### Normalize some sample values
print "Min-max normalized values: %r" % map(minmax_normalize, [2500, 50, 250, 35, 8, 100, 19])

