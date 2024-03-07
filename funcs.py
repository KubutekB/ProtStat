import matplotlib.pyplot as plt
import os
import re
import sys
import time

#Calculate average protein length in a file
def avg_prot_len(data):
    x = time.time()
    print("Calculating for " + data)
    f = open(data)
    g = f.readlines()
    f.close()

    total_prots = 0
    total_length = 0

    for i in g:
        if ">" in i:
            total_prots += 1
        else:
            add = len(i) - 1
            total_length += add
    print("Time elapsed: " + str(time.time() - x))
    return int(round(total_length / total_prots,0))

#Calculate aminoacid content in a file
def aa_cont(data):
    x = time.time()
    print("Calculating for " + data)
    f = open(data)
    g = f.readlines()
    f.close()

    total_length = 0
    aa = {}

    for i in g:

        if ">" in i:
            pass
        else:
            add = len(i) - 1
            total_length += add
            for j in i:
                if j == '\n':
                    pass
                elif j not in aa:
                    aa[j] = 1
                else:
                    aa[j] += 1

    for a in aa:
        aa[a] = round(aa[a]/total_length*100,2)

    print("Time elapsed: " + str(time.time() - x))

    return aa

#Calculate a chosen statistic for every file in list
def calc_stat(data, func):
    x = time.time()
    print("Calculating " + func.__name__ + "...")
    result = {}

    for i in data:
        val = func(i)

        with open(i, "r") as file:
            name = re.search("OS.*OX", file.readlines()[0]).group()[3:-3]
            result[name] = val
    print("Time elapsed: " + str(time.time()-x))
    return result

def calc_stat_domain(data, func):
    x = time.time()
    print("Calculating " + func.__name__ + "...")
    result = {}

    for i in data:
        val = func(i)
        name = i[6:-6]
        result[name] = val
    print("Time elapsed: " + str(time.time()-x))
    return result


#Calculate lengths of each protein in file
def all_lengths(data):
    x = time.time()
    print("Calculating for " + data)

    f = open(data)
    g = f.readlines()
    f.close()
    lengths = []
    l = 0

    for i in g:
        if ">" in i:
            lengths.append(l)
            l = 0
        else:
            l += len(i) - 1
    lengths.append(l)
    del lengths[0]
    print("Time elapsed: " + str(time.time() - x))
    return lengths