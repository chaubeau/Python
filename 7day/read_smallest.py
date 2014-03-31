#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#  Date: 2014-03-31 17:41:30
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
import sys
import tsdl

def smallest_value(r):
    '''Read and process reader r to find the smallest value after the TSDL header'''
    line = tsdl.skip_header(r).strip()
    smallest = int(line)

    for line in r:
        line = line.strip()
        value = int(line)
        if value  < smallest:
            smallest = value

    return smallest



if __name__ == "__main__":
    input_file = open(sys.argv[1],"r")
    print smallest_value(input_file)
    input_file.close

