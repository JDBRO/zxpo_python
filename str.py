#!/usr/bin/env python
#Filename: str.py
import string
strvar = '123'
print strvar.isdigit()
print strvar.isalnum()
str2 = ''
print str2.isdigit()
print str2.isalnum()
print str2.isspace()
str3 = ' '
print str3.isdigit()
print str3.isalnum()
print str3.isspace()
str4 = 'a1'
print str4, str4.isdigit(),str4.isalnum(),str4.isalpha(),'\n'
str5 = '1a'
print str5, str5.isdigit(),str5.isalnum(),str5.isalpha(),'\n'
str6 = '0'
print str6, str6.isdigit(),str6.isalnum(),str6.isalpha(),'\n'
str7 = 'a'
print str7, str7.isalnum(),str7.isalpha(),'\n'
