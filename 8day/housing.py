#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#  Date: 2014-04-01 14:06:34
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

def  housing(r):
    '''return difference between the housing starts and costruuction contracts in 1983~1984 from reader r.'''

    starts = []
    contracts = []

    for line in r:
        starts,contracts,rate = line.split()
        starts.append(float(starts))
        contracts.append(float(contracts))

    return (sum(starts[12:24]) - sum(starts[0:12]),sum(contracts[12:24]) - sum(contracts[0:12]))

if __name__ == "__main__":
    input_file = open(sys.argv[1],"r")
    print housing(input_file)
    input_file.close
