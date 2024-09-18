# XML and JSON Editing Script

## Description

This Python script processes an XML file based on modifications specified in a JSON file. It generates two output files: `.rcf` (with updates) and `.xml` (for testing purposes).

## Functions

### `parse_xml_return_root(file_name_with_path)`

- **Description**: Takes the XML file path as input, reads and parses the XML file, and returns the root element.
- **Error Handling**:
  - `FileNotFoundError`: If the file directory is incorrect.
  - `ET.ParseError`: If the XML data is corrupted or invalid.

### `parse_json_return_dict(file_name_with_path)`

- **Description**: Takes the JSON file path as input, reads and parses the JSON file, and returns it as a dictionary.
- **Error Handling**:
  - `FileNotFoundError`: If the file directory is incorrect.
  - `JSONDecodeError`: If the JSON data is corrupted or invalid.

### `loop_and_enable(root)`

- **Description**: Loops through the XML tree to find "rule" tags. If the tag's ID exists in the dictionary, it sorts the IDs and calls `enable_messages` to update the messages.

### `enable_messages(rule, messages_list)`

- **Description**: Takes a "rule" tag and a list of messages to be enabled. Updates or adds messages within the enforcement tag.

### `update_into_rcf(root, file_name_with_path)`

- **Description**: Generates `.rcf` and `.xml` files with updates based on the JSON file. The `.xml` file generation is optional for testing.

## Code Flow

1. **Initiation**: 
   - Run the `app.py` file and provide three command-line arguments:
     1. Input XML file path
     2. Input JSON file path
     3. Output file path (default extension `.rcf` is added)

2. **Parsing**:
   - Calls `parse_xml_return_root` and `parse_json_return_dict` with error checks.

3. **Searching and Editing**:
   - Calls `loop_and_enable` to find "rule" tags and edit them if needed by calling `enable_messages`.

4. **Generating Output Files**:
   - Calls `update_into_rcf` to generate `.rcf` and `.xml` files with modifications.

## Sample Usage

### 1. Proper Inputs

```bash
python app.py "C:\Users\ext.hassan.lotfy\PycharmProjects\File handling\Task1_xml_edit\my_xml.xml" "C:\Users\ext.hassan.lotfy\PycharmProjects\File handling\Task1_xml_edit\input.json" "C:\Users\ext.hassan.lotfy\PycharmProjects\File handling\Task1_xml_edit\new_file"
