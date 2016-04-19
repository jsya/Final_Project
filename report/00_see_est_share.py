# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 18:25:20 2015

@author: judyyang
"""

import pandas as pd
import csv

# The csv.reader has a delimeter parameter, which we set to '\t' to indicate that the file is tab-separated
with open('/Users/judyyang/Google Drive/GA_DS/Project/SHARE_wave5_EST.csv', mode='rU') as f:   # We temporarily refer to the file by the variable name f for file
    file_nested_list = [row for row in csv.reader(f, delimiter='\t')] 
    