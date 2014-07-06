#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#  Date: 2014-03-31 14:31:12
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

def skip_header(r):
    '''skip the hrader in reader r, and return the first real piece of data'''
    line  = r.readline()
    while line.startswith('#'):
        line = r.readline()

    return line

def process_file(r):
    '''read and print open reader r'''
    line = skip_header(r).strip()
    print line

    for line in r:
        line = line.strip()
        print line

if __name__ == "__main__":
    input_file = open(sys.argv[1],'r')
    process_file(input_file)
    input_file.close()

