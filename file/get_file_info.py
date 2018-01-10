#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File:	get_file_info.py
Author: wyscjm
Email:	w079064@163.com
Github: https://github.com/wyscjm
Date:	2018-1-10
Ver:	V0.1
Description: 
    get all file's info
"""
import os


file_type = [".c",".h",".sdh"]
version_start = "* Archive: Revision "
include_start = "#include "
mks_path_start = "* Archive: Member "
# "* Archive: Member added to project"


def get_module_list(dir):
    print("get module_list")
    module_list = []
    if os.path.isdir(dir):
        for parent,dirnames,filenames in os.walk(dir):
            for dir in dirnames:
                if dir == "core":
                    module = {}
                    module["path"] = parent
                    module["name"] = os.path.basename(parent)
                    module_list.append(module)
                    #print(module)
    else:
        print("should use a dir")
    return module_list


def get_module_info(module_list):
    print("get module info")
    new_module_list = []
    #print(module_list)
    for module in module_list:
        module_files = []
        for parent,dirnames,filenames in os.walk(module["path"]):
            for filename in filenames:
                if os.path.splitext(filename)[1] in file_type:
                    f_path = os.path.join(parent,filename)
                    f = open(f_path,'r')
                    module_file = {}
                    all_version = []
                    include_files = []
                    mks_paths = []
                    for line in f:
                        if version_start in line:
                            version = line.split(" ")[3]
                            all_version.append(version)
                        if include_start in line:
                            include_file = line.split()[1]
                            include_files.append(include_file)
                            #print(include_file)
                        if mks_path_start in line:
                            mks_paths.append(line)
                            #print(line)
                    module_file["filename"] = filename
                    module_file["versions"] = all_version
                    module_file["inc_files"] = include_files
                    module_file["mks_paths"] = mks_paths
                    module_files.append(module_file)
        module["files"] = module_files
        new_module_list.append(module)
    return new_module_list
                
                          
                
    

if __name__ == '__main__':
    module_list = get_module_list(".")
    module_list2 = get_module_info(module_list)
    
    #module_list output
    module_list_string = "module_list:\n"
    for module in module_list2:
        module_list_string += module["name"] +"\n"
        for module_file in module["files"]:
            module_list_string +=  "\tfilename: %s.\n"%( module_file["filename"])
            if module_file["versions"]:
                module_list_string +=  "\t\t version: %s.\n"%( module_file["versions"][0])
            if module_file["mks_paths"]:
                module_list_string +=  "\t\t path: %s"%( module_file["mks_paths"][0])
            
            module_list_string += "\t\t%s\n"% module_file["inc_files"]
            """
            module_list_string += "\t\t"
            for inc_file in module_file["inc_files"]:
                if inc_file:
                    module_list_string +=  "%s, "%(inc_file)
            print(module_file["inc_files"])
            module_list_string += ".\n"
            """
            
        #print(module["name"])
        #module_list_string + 
    open("./module_list_name.txt","w").write(module_list_string)
    
