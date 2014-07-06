#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#  Date: 2014-04-21 09:58:14
#
#  Copyright 2014 chaubeau <chaubeau01@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  Desc :
#
import ConfigParser
import hashlib
import sys
import yaml

def get_file_md5sum(file_path):
    ret = False
    strMd5 = ""
    try:
        fp = open(file_path, "rb")
        md5 = hashlib.md5()
        str_read = ""
        while True:
            str_read = fp.read(8096)
            if not str_read:
                break
            md5.update(str_read)
        ret = True
        strMd5 = md5.hexdigest()
    except:
        ret = False
    else:
        fp.close()
    return ret, strMd5

def monitor_mysql(username,password,host,port):


def back_config_file(bmi_cluster,config_file,proxy_path):

def load_yaml(yaml_file):

def modify_config_file(ip):

def compare_config_file(new_config_file,old_config_file):

def restart_dbproxy(bmi_cluster,dbproxy_path):

def check_restart_proxy(bmi_cluster,dbproxy_path):


if  __name__ == "__main__":
    config_file = sys.argv[1]
    print get_file_md5sum(config_file)



