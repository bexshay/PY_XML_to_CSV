# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 18:41:25 2021

@author: https://morioh.com/p/96eb0b5d6908
"""
#To read in the XML data, use Python’s built-in XML module with sub-module ElementTree.
#Then we convert ElementTree object to a dictionary using the xmltodictlibrary.
#From dictionary, we convert to CSV, JSON, or Pandas Dataframe
import xml.etree.ElementTree as ET
import xmltodict
import json
import csv
import pandas as pd

tree = ET.parse('math.xml')
xml_data = tree.getroot()

xmlstr = ET.tostring(xml_data, encoding='utf8', method='xml')

#convert ET object to dictionary
data_dict = dict(xmltodict.parse(xmlstr))

# print(data_dict)

#convert dictionary to json
with open('new_math.json', 'w+') as json_file:
    json.dump(data_dict, json_file, indent=4, sort_keys=True)

#convert json to csv
# Read the data from file. We now have a Python dictionary
with open('new_math.json') as f:
    data_listofdict = json.load(f)

print(data_listofdict['response']['row']['row'][0].keys())

with open('new_math.json') as f:
    data_fr = pd.DataFrame.from_dict(pd.json_normalize(f))

# Writing a list of dicts to CSV. Create column names
keys = data_listofdict['response']['row']['row'][0].keys()
print(keys)
with open('saved_math.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data_listofdict['response']['row']['row'])

#save to data frame
df = pd.DataFrame.from_dict(data_listofdict['response']['row']['row'])

