#!/usr/bin/env python
#Filename: helloworld.py
#if you do not know where Python is located,you can use the special env program on Linux/Unix systems.
#the env program will in turn look for the Python interpreter which will run the program.
print('Hello World')
#in python2.x both / and // represent Int division, whereas in python3.x / represents float division
#in python2.x you can from __future__ import division let / change to float division
'{0:.3f}'.format(1/3)       # in python 2.x
'{0:.3}'.format(1/3)        # in python 3.x
'{0:.3}'.format(float(1)/3) # in python 2.x
#python -mjson.tool some.json can show json file clearly, from python2.6 start, python add json.tool.
class DES:
    def __init__(self,name):
        self.name=name

