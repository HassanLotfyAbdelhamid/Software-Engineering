# XML to RCF python Script explanation

## Description
This Python script processes an XML file based on modifications specified in a JSON file then generates .rcf file with the modifications 

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

- **Description**: Generates `.rcf` file with updates based on the JSON file.

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

## Sample Scenarios:

### 1. Proper Inputs

```bash
python app.py "C:\Users\ext.hassan.lotfy\PycharmProjects\File handling\Task1_xml_edit\my_xml.xml" "C:\Users\ext.hassan.lotfy\PycharmProjects\File handling\Task1_xml_edit\input.json" "C:\Users\ext.hassan.lotfy\PycharmProjects\File handling\Task1_xml_edit\new_file"
output: .rcf file

### 2. Incorrect file path for XML 
python app.py "C:\Use\ext.hassan.lotfy\PycharmProjects\File handling\Task1_xml_edit\my_xml.xml" "C:\Users\ext.hassan.lotfy\PycharmProjects\File handling\Task1_xml_edit\input.json" "C:\Users\ext.hassan.lotfy\PycharmProjects\File handling\Task1_xml_edit\new_file"
(use in first directory incorrect file path)
output: File directory might be incorrect, or file content is not valid

### 3. invalid json file syntax:
python app.py "C:\Use\ext.hassan.lotfy\PycharmProjects\File handling\Task1_xml_edit\my_xml.xml" "C:\Users\ext.hassan.lotfy\PycharmProjects\File handling\Task1_xml_edit\corrupted.json" "C:\Users\ext.hassan.lotfy\PycharmProjects\File handling\Task1_xml_edit\new_file"
(corrupted.json containing only text "this is corrupted file" and saved as .json)
output: The file could not be parsed. It may be malformed or contain invalid json


# Git steps explanation

## Description

This section is to explain git commands, creating a new branch, uploading files to it, making Pull request, squashing commits, review comments

## steps

**Note**: terminal should be opened inside local git repo

1. **check first that current branch is the master (main)**
```git branch```
output should be main, or master, or whatever name given to the main branch

2. **create new branch and switch to it**
```git checkout -b new-branch-name```
ex:```git checkout -b "XML to RCF Editor2"``` this will create branch named "XML to RCF Editor2"

3. **uploading files**
```git add "file1"```
```git commit -m "commit text"```
```git push origin branch_name```
ex: ```git push origin "XML to RCF Editor2"``` this will push the committed files to "XML to RCF Editor2" branch

4. **creating pull request**
PR: requesting to merge a branch to another
- In GitHub, open the repo (Software-Engineering for example), to the top left, click on "pull requests" (code, issues, **pull requests**)
- click on "New pull request"
- to the top left, select main branch in "base", and the branch to be merged in "compare"
- add name and description for the PR
- click on create PR

5. **squashing commits**
squashing commits is to compress selected commits into 1 commit, in our case we compressed all commits into 1
- view commit history to check the commits to be squashed: ```git log --oneline```
- assuming the commits to be squashed are within the last N commits: git rebase -i HEAD~N
- grouping: for windows: press I to edit, then replace "pick" with "squash" for commits to be squashed, by default commits will be squashed into the first commit, press esc, wq! to save
- commiting the group: comment all messages using # and leave one messages uncommented, edit uncommented messsage content, :wq! for saving, now all commits are squashed into one commit with the edited message (in my case all commits grouped into one commit with "xml to rcf converter files" message, which is the only commit on the branch after squashing)
- push changes to GitHub repo: ```git push origin branch_name --force```

6. **review comments**
before merging, the PR should be approved first from supervisor, who will review the code and add comments if there is any issues to be fixed
- open the created pull request from "pull request" tab
- in "conversation" section to the top left, review comments can be found if any.
- after making the modifications according to a review comment, you can click on "resolve conversation" under this review comment
- after resolving all review comments, upload the modified files using the same steps (add commit push)


# enable the converter node on CI

## Description
This section includes how to install wsl, ansible and python on virtual Linux installed, explaining the implemented playbook

## WSL installation:

### Description
This section includes how to install wsl, good and bad practices, challenges and solutions

### installation as virtual machine:

1. **enable windows features**

 - start > search "turn windows features on or off" > check "windows subsystem" & "virtual machine" boxes

2. **install Ubuntu**
 - Open Microsoft Store > search "Ubuntu" > download latest version > install > restart

3. **install WSL package**
 - Open terminal > type "bash" > copy the URL from the error message that appears > paste URL in browser > download "WSL linux kernel for windows x64" > install > restart

4. **verify that installation successful**
 - type any Linux command preceded by 'wsl', for example: wsl ls
   output should be listed files and folders in current Linux directory

 - if you get "'wsl' not recognized" error, then you will need to define Linux system path in environment variables:
	1. open Ubuntu terminal > follow steps to create new user (name and password) > command: pwd > copy output path > convert to windows path (ex: /mnt/c/Users/YourUsername/path-to-folder to C:\Users\YourUsername\path-to-folder)
        2. start bar > search "edit the system environment variable" > edit > new > copy the path > save

 - now check again if wsl is recognized

5. **install wsl to use from windows terminal**
 - open windows cmd or powershell > command: wsl --install

### bad practices:

- **Description**: we had to search for alternatives to use wsl since our machine is restricted access corporate machine:
 
 1. **installing ubuntu dual boot**: you will be using Linux as main OS, but installing virtual machine will allow you to work on windows and operate nodes with commands preceded with wsl in windows terminal

 2. **installing ubuntu on sandbox**: not allowed because enabling windows features is not available in windows sandbox

 3. **using online wsl**: will introduce complexity because of the following:
	- accessing local files from remote machine will require file sharing setup
	- increased latency and delay
	- Ads

## Ansible playbook explanation

### Description
This section includes how to install ansible after successfully installing wsl, installing python, and playbook structure explanation

### installing ansible, python and pip to manage python libraries

 - Open Ubuntu terminal > command: sudo apt install ansible > command: sudo apt install python3 > command: sudo apt install python3-pip
 - verify installation: "name" --version (ex: pip3 --version) 

### Ansible playbook

- **Description**: playbook enable_converter_ci mainly consists of 3 tasks:
	- running the python script for file converter
	- checking if output file is generated successfully
	- if file is generated, file is found will be printed, otherwise this task is skipped
	playbook enable_converter_ci_role same as enable_converter_ci but third task calls a role to print the message

- **print_the_message role**:
1. create role using: ```ansible-galaxy init <role_name>```
2. optional: if role couldn't be found when running main yml file, add its directory to ansible.cfg:
	- locate ansible.cfg: ```cd ~``` > ``` find / -name "ansible.cfg" 2>/dev/null```
	- add directory to ansible.cfg: under [defaults] roles_path var, type :<ansible directory> 




- **How to run**:
	- Open windows terminal > command: wsl ansible-playbook "yaml_file_path" (ex: /mnt/c/Users/ext.hassan.lotfy/PycharmProjects/enable_converter_ci_role.yml)

- **Output**:
	- if the file path being checked in second task is the same as the generated file from the script (refer to sample1.png), output will be as in output1.png
	- if the file path being checked in second task is the different from the generated file from the script (refer to sample2.png), output will be as in output2.png