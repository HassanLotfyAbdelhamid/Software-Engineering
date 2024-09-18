
import xml.etree.ElementTree as ET

import functions
import argparse

import json

parser = argparse.ArgumentParser(description="Script to edit xml files and save it as .rcf")

## pass args in terminal:
## python try_task1.py myfile --output_file_name "edited" (ignore file_path)

# create arguments
parser.add_argument('input_xml_file_name', help="input xml file name", type=str)
parser.add_argument('input_json_file_name', help="input xml file name", type=str)
parser.add_argument('output_rcf_file_name', help="output rcf file name", type=str)
#parser.add_argument('--file_path', help="file path until the folder containing the xml file", type=str)

# load arguments into parse_arguments list
args = parser.parse_args()




########### parsing #############

# parse the xml file and get the root
root = functions.parse_xml_return_root( args.input_xml_file_name )

# parse the json file into dictionary
json_dictionary = functions.parse_json_return_dict(args.input_json_file_name)


########## modifying ###########
if json_dictionary is not None and root is not None:
    functions.loop_and_enable(root, json_dictionary)

# # search for message id= '0302' and edit its value
# functions.find_and_edit(root,'id','Rule-11.1',
#                         'enforcement','id','0302','mapped','yes')
# # search for message id = '0303' which doesnt exist, so it will be added
# functions.find_and_edit(root,'id','Rule-11.1',
#                         'enforcement','id','0303','mapped','yes')


########### saving ###########
if json_dictionary is not None and root is not None:
    functions.update_into_rcf(root,args.output_rcf_file_name)








