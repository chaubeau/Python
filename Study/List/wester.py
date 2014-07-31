#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wester.py
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
#  
#  

def print_lol(the_list):
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item)
		else:
			print(each_item)
		

def main():
	movies=["chaubeau",1989,"sz",["Lisy","MySQL"],["oracle","DB2"],[["opensuse","Fedora","ubuntu","arch"]]]
	print_lol(movies)
	return 0

if __name__ == '__main__':
	main()

