#!/usr/bin/expect -f
trap {
   set rows [stty rows]
   set cols [stty columns] 
   stty rows $rows columns $cols < $spawn_out(slave,name)
} WINCH

set timeout 10
set pin [lindex $argv 1]
set token [lindex $argv 0]

spawn ssh xiaobo01@relay00.baidu.com
#expect  "*Enter PASSCODE:" {
expect  "*relay00.baidu.com's password:" {
send "$pin$token\n" }
expect "*bash-baidu-ssl" {
send "ssh xiaobo01@yf-dba-es-cc00.yf01\n" }
expect "*password*" {
send "dbaKHTdolphinpt\n" }
expect "*xiaobo01@yf-dba-es-cc00.yf01.baidu.com*"
send "sudo -iu mysql\n"
expect -re "$"
interact
