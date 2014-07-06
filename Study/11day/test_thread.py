#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#  Date: 2014-04-22 15:54:52
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
import time
import thread
def timer(no, interval):
    cnt = 0
    while cnt<10:
        print 'Thread:(%d) Time:%s/n'%(no, time.ctime())
        #time.sleep(interval)
        cnt+=1
    thread.exit_thread()


def test():
    thread.start_new_thread(timer, (1,2))
    thread.start_new_thread(timer, (2,1))

if __name__== '__main__':
    test()
