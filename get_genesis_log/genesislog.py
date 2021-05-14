#!/usr/bin/python
# coding: utf-8

#
# A parser script for GENESIS output style
#
# (c) Copyright 2021 RIKEN. All rights reserved.
#
import sys
import re
import matplotlib.pyplot as plt


def read_genesis(filename, key):
    ld = open(filename)
    step='STEP'
    lines = ld.readlines()
    ld.close()

    index = {}
    x = []
    y = []
    patternINFO = re.compile('^INFO.')
    for line in lines:
        result = patternINFO.search(line)
        if result is not None:
            line_sub = re.sub("\n$","",line)
            line_sub = patternINFO.sub('',line_sub)
            data_each = line_sub.split()
            flag_out=True
            for i in range(len(data_each)):
                if data_each[i][-1].isalpha(): #alphabet
    #                print("%d %s" % (i,data_each[i]))
                    index[data_each[i]] = i
                    flag_out=False
    
            if (flag_out):
                ind_step = index[step]
                x.append(float(data_each[ind_step]))
                if key in index:
                    ind_key = index[key]
                    y.append(float(data_each[ind_key]))
    #                print(" %s %s" % (data_each[ind_step], data_each[ind_key]))
    
    return x, y

