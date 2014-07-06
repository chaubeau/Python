#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#  Date: 2014-04-18 19:19:26
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
partLable = ("<",">")
sectionLable = ("[","]")
endlineLable = "\n"
equalLable = "="
noteLable = '#'

# 得到总配置的map
def getPlatformMap(strtmp,lable1 = partLable,lable2 = sectionLable):
    tmp = strtmp.split(lable1[0])
    tmp = [elem for elem in tmp if len(elem) > 1]
    tmp = [elem for elem in tmp if elem.rfind(lable1[1]) > 0]
    platdict = {}
    for elem in tmp:
        key = elem[0:elem.find(lable1[1]):]
        value = elem[elem.find(lable2[0])::]
        platdict[key] = value
    return platdict

# 得到各部分的map
def getSectionMap(strtmp,lable1 = sectionLable):
    tmp = strtmp.split(lable1[0])
    tmp = [elem for elem in tmp if len(elem) > 1]
    tmp = [elem for elem in tmp if elem.rfind(lable1[1]) > 0]
    sectionDict = {}
    for elem in tmp:
        key = elem[0:elem.find(lable1[1]):]
        value = elem[elem.find(endlineLable)+len(endlineLable)::]
        sectionDict[key] = value
    return sectionDict

# 获取具体配置值
def getValueMap(strtmp):
    tmp = strtmp.split(endlineLable)
    tmp = [elem for elem in tmp if len(elem) > 1]
    valueDict = {}
    for elem in tmp:
        if elem.find(noteLable) > 0: # 如果有注释则去掉注释
            elem = elem[0:elem.find(noteLable):]
        elem = ''.join(elem.split()) # 去掉空白字符
        key = elem[0:elem.find(equalLable):]
        value = elem[elem.find(equalLable)+len(equalLable)::]
        valueDict[key] = value
    return valueDict

f = open(raw_input("Input file name : "),"rb")
strFileContent = f.read()
f.close()
vardict = {}

var1 = getPlatformMap(strFileContent)

for k,v in var1.items():
    var2 = getSectionMap(v)
    dict3 = {}
    for k2,v2 in var2.items():
        var3 = getValueMap(v2)
        dict3[k2] = var3
    vardict[k] = dict3

print vardict["part2"]["global"]["ip"]

