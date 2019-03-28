# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 22:38:14 2019

@author: Pooyan
"""

 
class ID:
    def __init__(hh,name,age):
        hh.name=name
        hh.age=age
        
    def callback(hh):
        print("Name:  "+hh.name  +"Age:  "+hh.age)
        del hh.name
name_p=input("Enter your name:")
age_p=input("Enter your age:")

new_p=ID(name_p,age_p)
new_p.callback()

#print(new_p.name)
#print(new_p.age)








