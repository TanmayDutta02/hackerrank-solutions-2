#Detect the Email Addresses

import re
p = re.compile('[_0-9a-zA-Z]+[_\.0-9a-zA-Z]*@[0-9a-zA-Z_]+[\.0-9a-zA-Z_]+[0-9a-zA-Z_]+')
n = int(input())
l = []
for i in range(n):
    x = str(input())
    r = re.findall(p, x)
    for z in r:
        if(z not in l):
            l.append(z)
l.sort()
for i in range(len(l)):
    if(i == len(l)-1):
        print(l[i])
    else:
        print(l[i],end=";")

-----------------------------------------------------------------------------------------------------------------------------------------------------

#Find a Word

import re
n = int(input())
sen = list()
for i in range(n):
    x = str(input())
    sen.append(x)
t = int(input())
for i in range(t):
    x = str(input())
    p = re.compile('(?:\W|\A)'+x+'(?=\W|\Z)')
    c = 0
    for y in sen:
        c += len(re.findall(p, y))
    print(c)

--------------------------------------------------------------------------------------------------------------------------------------------------------

#Matching Same Text Again & Again

Regex_Pattern = r'^([a-z]\w\s\W\d\D[A-Z][a-zA-Z][aieouAEIOU]\S)\1$'	# Do not delete 'r'.

--------------------------------------------------------------------------------------------------------------------------------------------------------

#Negative Lookbehind

Regex_Pattern = r"(?<![aeiouAEIOU])."	# Do not delete 'r'.

--------------------------------------------------------------------------------------------------------------------------------------------------------

#Positive Lookbehind

Regex_Pattern = r"(?<=[13579])\d"	# Do not delete 'r'.

---------------------------------------------------------------------------------------------------------------------------------------------------------

#Negative Lookahead

Regex_Pattern = r"(.)(?!\1)"	# Do not delete 'r'.

--------------------------------------------------------------------------------------------------------------------------------------------------------

#Positive Lookahead

Regex_Pattern = r'o(?=oo)'	# Do not delete 'r'.

---------------------------------------------------------------------------------------------------------------------------------------------------------

#Hex Color Code

import re

T = int(input())
in_css = False
for _ in range(T):
    s = input()
    if '{' in s:
        in_css = True
    elif '}' in s:
        in_css = False
    elif in_css:
        for color in re.findall('#[0-9a-fA-F]{3,6}', s):
            print(color)
