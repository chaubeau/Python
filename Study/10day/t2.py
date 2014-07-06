#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#  Date: 2014-04-21 09:44:42
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

cf = ConfigParser.ConfigParser()
cf.read("proxy.ini")
secs = cf.sections()
#print 'sections:', secs
opts = cf.options("Master_Host_1")
#print 'options:', opts
#kvs = cf.items("Master_Host_1")
#print 'sec_a:', kvs

str_val = cf.get("Master_Host_*", "host")
print 'host:', str_val

#cf.set("Master_Host_1", "host", "127.0.0.1")
#cf.write(open("proxy.ini", "w"))

#str_val1 = cf.get("Master_Host_1","host")

#print 'host:', str_val1


