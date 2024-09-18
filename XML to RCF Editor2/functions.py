import xml.etree.ElementTree as ET
import copy
import json

"""
function name: parse_xml_return_root
function description: parses XML file and returns root, given the file path
inputs: file_name_with_path
outputs: root
"""

def parse_xml_return_root(file_name_with_path):

    # error handling in case directory in incorrect or file content syntax is invalid
    try:
        # parse the xml file
        tree = ET.parse(rf"{file_name_with_path}")
        root = tree.getroot()
        return root
    except FileNotFoundError:
        print("File not found")
        return None
    except ET.ParseError:
        print("The file could not be parsed. It may be malformed or contain invalid XML")
        return None


"""
function name: parse_json_return_dict
function description: parses XML file and returns dictionary, given the file path
inputs: file_name_with_path
outputs: json_dictionary 
"""

def parse_json_return_dict(file_name_with_path):

    # error handling in case directory in incorrect or file content syntax is invalid
    try:
        # parse the json file
        with open(file_name_with_path, 'r') as file:
            json_dictionary = json.load(file)
            return json_dictionary
    except FileNotFoundError:
        print("File not found")
        return None
    except json.JSONDecodeError:
        print("The file could not be parsed. It may be malformed or contain invalid json")
        return None



"""
function name: loop_and_edit
function description: looping on the xml file elements. Once rule tag is found, check if its id is inside the given
dictionary (json file) or not, if found, edit messages values inside enforcement, if not continue looping till finding the
following rule tag and so on.
inputs: xml_file, dictionary
outputs: None
"""

def loop_and_enable(element, json_dictionary):
    # loop on parents
    for sub in element:

        # check if current parent is rule or not
        if sub.tag == "rule":

            # if it's rule, check if it exists in json dictionary or not
            rule_id = sub.get("id")
            if rule_id in json_dictionary:

                ## if found in the dictionary, get the messages IDs to be edited
                # activate this rule then enable messages
                element.set('active', 'yes')
                messages_id = json_dictionary[rule_id]
                enable_messages(sub,messages_id)


        # if parent has children, loop on them
        if len(sub) > 1:
                loop_and_enable(sub, json_dictionary)

"""
function name: edit_mapped
function description: function taking rule parent, searching for enforcement inside, then search for messages ids in the
given list, and enable them
inputs: element (rule), messages_key_val (list containing messages to be enabled)
return: None (editing the xml)
"""

def enable_messages(element, messages_key_val, tag = "enforcement" ,message_key = "id", key_to_change = "mapped", key_to_change_val = "yes"):


    # search for tag (enforcement) inside element (rule)
    enforcement = element.find(f'{tag}')

    # check if tag (enforcement) exists or not
    if enforcement is None: # if not found print tag not found
        print(f"{tag} not found")

    else: # if tag (enforcement) found, search inside for the messages id and enable them

        # loop on the given messages ids
        for msg in messages_key_val:

            message = enforcement.find(f".//*[@{message_key}='{msg}']")

            # check if the message exists or not
            if message is not None: # if found, set key_to_change (mapped) to key_to_change_val ("yes")
                message.set(key_to_change, key_to_change_val)
                print(f"message with id = {msg} under rule id {element.get("id")} found and modified")

            else: # if not found, add it

                # copy the first message
                first_message = enforcement[0] if len(enforcement) > 0 else None
                # get a clone
                new_message = copy.deepcopy(first_message)
                # edit the clone attributes: set id, then set the required attribute
                new_message.set(message_key, msg)
                new_message.set(key_to_change, key_to_change_val)
                # append the clone to the XML file
                enforcement.append(new_message)
                print(f"message with id = {msg} under rule id {element.get("id")} does not exist. message added")



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

