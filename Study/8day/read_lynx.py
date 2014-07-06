#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#  Date: 2014-04-01 13:43:19
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

def find_largest(line):
    '''Return the largest value in line…………'''
    largest = -1
    for value in line.split():

        v = int (value[:-1])

        if v >largest:
            largest = v
    return largest

def process_file(r):
    '''Read and process reader r'''
    line  = skip_header(r).split
    largest = find_largest(line)

    for line in r:
        large  = find_largest(line)
        if large > largest:
            largest =large
    return  largest


if __name___ == "__main__":
    input_file = open(sys.argv[1],"r")
    print process_file(input_file)
    input_file.close

