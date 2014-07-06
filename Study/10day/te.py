#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#  Date: 2014-04-21 09:33:12
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

import os
import time
import sys
import ConfigParser
import json


global json_conf
global ini_conf
global g_diff_dict
global g_dbproxy_port

g_ts_node_conf = ['host', \
                    'ts_port', \
                    'load_balance_weight', \
                    'ts_connect_timeout', \
                    'ts_max_connections', \
                    'max_conn_pool_size', \
                    'ts_reserved_master_connections', \
                    'ts_time_reconnect_interval',
                    'exchange_enable']

def get_file_mdrsum(file_path):
    ret = False
    strMd5 = ""
    try:
        fp = open(file_path,"r")
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

    return ret.strMd5




