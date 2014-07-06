#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#  Date: 2014-03-27 16:31:27
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
for x in enumerate('abc'):
    print x

values = [1,2,3]

for pair in enumerate(values):
    i = pair[0]
    v = pair[1]
    values[i] = 2 * v

print values


val = [100,200,300]

for (i,v) in enumerate(val):
    val [i] = 2 *v

print val
