from email import header
from collections import defaultdict
from hashlib import new
from posixpath import split
import pandas as pd
import numpy as np
from operator import itemgetter
from itertools import count, groupby, zip_longest
import csv

from utils import remove, get_horzs, get_data, split_labels, split_for_type


# Read in file values
file1 = open('./survey_txt_files/facebook.txt')
data1 = file1.readlines()

file2 = open('./survey_txt_files/confidant.txt')
data2 = file2.readlines()

file3 = open('./survey_txt_files/sexual.txt')
data3 = file3.readlines()

file4 = open('./survey_txt_files/ego.txt')
data4 = file4.readlines()

file1.close()
file2.close()
file3.close()
file4.close()

# Same marker for horz bar (see below)
# ----------------------------------------------------------------------------------------------------
# Use this value to find where variables are (in between pair of indices)
horz_marker = data1[5]

# Make list readable for numpy and read index of horz bar
lst = np.array(data1)
lst2 = np.array(data2)
lst3 = np.array(data3)
lst4 = np.array(data4)

index_horz = np.where(lst == horz_marker)
index_horz_arr = np.asarray(index_horz)

index_horz2 = np.where(lst2 == horz_marker)
index_horz_arr2 = np.asarray(index_horz2)

index_horz3 = np.where(lst3 == horz_marker)
index_horz_arr3 = np.asarray(index_horz3)

index_horz4 = np.where(lst4 == horz_marker)
index_horz_arr4 = np.asarray(index_horz4)

new_nospace_lst = []
new_nospace_lst2 = []
new_nospace_lst3 = []
new_nospace_lst4 = []

for n in lst:
    new_nospace_lst.append(remove(n))

for n in lst2:
    new_nospace_lst2.append(remove(n))

for n in lst3:
    new_nospace_lst3.append(remove(n))

for n in lst4:
    new_nospace_lst4.append(remove(n))


# Subtract and get indices for variables
getArr = get_horzs(index_horz_arr)
getArr2 = get_horzs(index_horz_arr2)
getArr3 = get_horzs(index_horz_arr3)
getArr4 = get_horzs(index_horz_arr4)


# Retrive data from initial array
var_data = get_data(lst, getArr)
var_data2 = get_data(lst2, getArr2)
var_data3 = get_data(lst3, getArr3)
var_data4 = get_data(lst4, getArr4)

# split by space to get labels
var_names = split_labels(var_data)[0]
var_labels = split_labels(var_data)[1]

var_names2 = split_labels(var_data2)[0]
var_labels2 = split_labels(var_data2)[1]

var_names3 = split_labels(var_data3)[0]
var_labels3 = split_labels(var_data3)[1]

var_names4 = split_labels(var_data4)[0]
var_labels4 = split_labels(var_data4)[1]

# Get types of variables
var_types = split_for_type(new_nospace_lst)
var_types2 = split_for_type(new_nospace_lst2)
var_types3 = split_for_type(new_nospace_lst3)
var_types4 = split_for_type(new_nospace_lst4)


# Writing & exporting the data frame to csv
d = [var_names, var_labels, var_types]
export_data = zip_longest(*d, fillvalue='')
with open('compiled/data_export.csv', 'w', encoding="UTF-8", newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(("fb_var_name", "fb_var_label", 'fb_var_type'))
    wr.writerows(export_data)
myfile.close()

d2 = [var_names2, var_labels2, var_types2]
export_data2 = zip_longest(*d2, fillvalue='')
with open('compiled/data_export2.csv', 'w', encoding="UTF-8", newline='') as myfile2:
    wr = csv.writer(myfile2)
    wr.writerow(("cf_var_name", "cf_var_label", 'cf_var_type'))
    wr.writerows(export_data2)
myfile2.close()

d3 = [var_names3, var_labels3, var_types3]
export_data3 = zip_longest(*d3, fillvalue='')
with open('compiled/data_export3.csv', 'w', encoding="UTF-8", newline='') as myfile3:
    wr = csv.writer(myfile3)
    wr.writerow(("sx_var_name", "sx_var_label", 'sx_var_type'))
    wr.writerows(export_data3)
myfile3.close()

d4 = [var_names4, var_labels4, var_types4]
export_data4 = zip_longest(*d4, fillvalue='')
with open('compiled/data_export4.csv', 'w', encoding="UTF-8", newline='') as myfile4:
    wr = csv.writer(myfile4)
    wr.writerow(("eg_var_name", "eg_var_label", 'eg_var_type'))
    wr.writerows(export_data4)
myfile4.close()
