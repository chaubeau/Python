#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#  Date: 2014-03-24 14:30:11
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
whales = [5,4,7,8,56,34,1,0,9]
krpython = ['ball','cry','kity','cart']
print whales

print whales[0]
print whales[1]
print whales[2]
print whales[4]
print whales[6]
print whales[-2]

print krpython[2]

nobles = ['helimu','none','argon','xenon']

print nobles
nobles[1] = 'neno'


print nobles

print len(nobles)

print max(whales)

new = krpython + nobles


print new

for v in new:
    print "My name is:",v


