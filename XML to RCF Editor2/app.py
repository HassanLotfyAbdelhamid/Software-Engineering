import functions


args = functions.handle_arguments()

# parse the xml file and get the root
root = functions.parse_xml_return_root( args.input_xml_file_name )
# parse the json file into dictionary
json_dictionary = functions.parse_json_return_dict(args.input_json_file_name)

if json_dictionary is not None and root is not None:
    # edit
    functions.loop_and_enable(root, json_dictionary)
    # save
    functions.update_into_rcf(root,args.output_rcf_file_name)








