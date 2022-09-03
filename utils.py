import chunk
import re

# UTIL
# Python3 code to remove whitespace


def remove(string):
    return string.replace(" ", "")


# Get horz bar indices
def get_horzs(index_horz_arr):
    diff_indices = []
    counter = 0
    for a in index_horz_arr:
        for b in a:
            val1 = a[counter]
            val2 = a[counter+1]
            num_between = (val1 + val2) / 2
            diff_indices.append(num_between)
            if(counter >= len(a)-2):
                break
            else:
                counter = counter + 2
    return diff_indices


def get_data(lst, diff_indices):
    counter = 0
    var_list = []
    while(counter < len(lst)):
        for i in diff_indices:
            if(counter == i):
                var_list.append(lst[counter])
        counter = counter + 1
    return var_list

# split string by single space


def split_labels(var_data):
    var_names = []
    var_labels = []
    for str in var_data:
        chunks = re.split('     +', str)
        if(len(chunks) > 2):
            if(chunks[0] == ''):
                chunks.remove(chunks[0])
            var_names.append(chunks[0])
            var_labels.append(chunks[1])
    return [var_names, var_labels]


def split_for_type(new_nospace_lst):
    var_types = []
    for ele in new_nospace_lst:
        if(ele.__contains__("type")):
            if(ele.__contains__(":")):
                var_types.append(ele.split(':')[1])
    return var_types
