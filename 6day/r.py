#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#  Date: 2014-03-27 13:34:49
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
for c in 'alpha':
    print c*2

print range(1,10,2)

sum = 0
for i in range(1,101):
    sum +=i
print sum


val = ['a','b','c','d']

print len(val)

print range(len(val))

for i in range(len(val)):
    val[i] *= 2
    print i,val[i]
