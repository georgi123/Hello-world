#!/usr/bin/env python


import os

option=raw_input("for help: ")

def ipinfo(option):

	if option == "help":
    		print("use address for ipshow\n use addrss for ip's\n use route to show pats\n")
	elif option == "address":
   		os.system("ip a")
	elif option == "route":
   		os.system("ip r")
	elif option == "link":
   		os.system("ip link show")
	else:
  		print("thereis not valid option for that operation")   
