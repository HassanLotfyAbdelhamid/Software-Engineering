
import xml.etree.ElementTree as ET

import functions
import argparse

parser = argparse.ArgumentParser(description="Script to edit xml files and save it as .rcf")

## pass args in terminal:
## python try_task1.py myfile --output_file_name "edited" (ignore file_path)

# create arguments
parser.add_argument('input_file_name', help="input xml file name", type=str)
parser.add_argument('output_file_name', help="output rcf file name", type=str)
#parser.add_argument('--file_path', help="file path until the folder containing the xml file", type=str)
# load arguments into parse_arguments list
args = parser.parse_args()

########### parsing #############

# parse the file and get the root
root = functions.parse_xml_return_root( args.input_file_name )
# root = functions.parse_xml_return_root("my_xml",
#                                        r"C:\Users\ext.hassan.lotfy\PycharmProjects\File handling\Task1_xml_edit")

########## modifying ###########

# search for message id= '0302' and edit its value
functions.find_and_edit(root,'id','Rule-11.1',
                        'enforcement','id','0302','mapped','yes')
# search for message id = '0303' which doesnt exist, so it will be added
functions.find_and_edit(root,'id','Rule-11.1',
                        'enforcement','id','0303','mapped','yes')

########### saving ###########

functions.update_into_rcf(root,args.output_file_name)








