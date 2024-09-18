import xml.etree.ElementTree as ET
import copy

"""
function name: parse_xml_return_root
function description: parses XML file and returns root, given the file name and path (directory)
inputs: file_name, path
outputs: root
"""

def parse_xml_return_root(file_name_with_path):

    # parse the xml file
    tree = ET.parse(rf"{file_name_with_path}")
    if tree is not None:
        root = tree.getroot()
        return root
    else:
        print("File not found")
        return None



"""
function name: find_and_edit
function description: identifies message address using attribute and its value (ex: 'id'='0304'). searches for parent first
using any parent att and its value (ex: id = 'Rule-11.1'). If not found returns error flag, otherwise it sets active to yes then
searches inside for specific tag (tag) (ex: enforcement). If not found returns error flag, otherwise it searches for tag 
using one of its attributes and its value (ex: id= '0302'). if found, edit att and value (req_att_name and req_att_val), if not
found, create a new tag line with the required attribute value.
inputs: xml_file, parent_att_name, parent_att_val, tag ,tag_att_name, tag_att_val, req_att_name, req_att_val
return: True, False (in case parent or tag not found)
"""

def find_and_edit(xml_file, parent_att_name, parent_att_val, tag ,tag_att_name, tag_att_val, req_att_name, req_att_val):
    # search for parent using one of its attributes (id for example)
    parent = xml_file.find(f".//*[@{parent_att_name}='{parent_att_val}']")

    # check if it exists or not
    if parent is None: # if not found return error flag
        print("parent 1 not found")
        return False
    else: # if found, search for the next parent inside
        parent.set('active', 'yes')
        parent2 = parent.find(f'{tag}')
        # check if next parent exists or not
        if parent2 is None: # if not found return error flag
            print("parent 2 not found")
            return False
        else: # if found, search for the message using one if its attributes (id for example)
            tag = parent.find(f".//*[@{tag_att_name}='{tag_att_val}']")
            # check if the message exists or not
            if tag is not None: # if found, change given attribute to required value
                tag.set(req_att_name, req_att_val)
                print("message found and modified")
            else: # if not found, add it
                # copy the first message
                first_message = parent2[0] if len(parent2) > 0 else None
                # get a clone
                new_message = copy.deepcopy(first_message)
                # edit the clone attributes: set id, then set the required attribute
                new_message.set(tag_att_name, tag_att_val)
                new_message.set(req_att_name, req_att_val)
                # append the clone to the XML file
                parent2.append(new_message)
                print("message does not exist. message added")

            return True


"""
function name: update_into_rcf
function description: creates rcf file with the modifications made to the xml file, generated file name, its path,
and XML root are arguments 
inputs: root, file_name, path
outputs: None (creates .rcf file but no return)
"""

def update_into_rcf(root, file_name_with_path):
    tree = ET.ElementTree(root)

    ###### generate rcf #########
    # Ensure extension is .xml
    if file_name_with_path.endswith('.rcf'):  pass
    else:   file_name_with_path += ".rcf"


    # if the file already exists, it will be overwritten
    try:
        with open(rf"{file_name_with_path}", "wb") as file:  # wb write binary mode, necessary when operating xml using python
            tree.write(file, encoding='utf-8', xml_declaration=False)
    except:
        print("incorrect output directory")

    ####### generate xml (optional for testing) ########
    try:
        file_name_with_path = file_name_with_path.replace(".rcf", ".xml")
        # if "edited_xml_file.xml" exists, it will be overwritten
        with open(rf"{file_name_with_path}", "wb") as file:  # wb write binary mode, necessary when operating xml using python
            tree.write(file, encoding='utf-8', xml_declaration=False)
    except:
        print("incorrect output directory")

