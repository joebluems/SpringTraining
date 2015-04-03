#!/usr/bin/python
import csv
import re

mlb={}
with open('./mlb', 'rb') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
	name = row[0]
	if name not in mlb or (name in mlb and row[1]=='TOT'): 
	  mlb[name]=row[1:]

print len(mlb)

spring={}
with open('./spring', 'rb') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
	name = re.split(' ',re.sub('Jr.? ','',row[0]))
	if len(name)==2:
	  final_name = "%s %s" % (name[1],name[0])
	elif len(name)>2:
          final_name = "%s %s" % (name[len(name)-1],' '.join(name[0:len(name)-1]))

	spring[final_name]=row[1:]

for a in mlb:
  if a not in spring:
     print "MISS",a,mlb[a]
  if a in spring:
    if int(mlb[a][1])>150 and int(spring[a][1])>20: 
      team = mlb[a][0]
      if team=="TOT": team=spring[a][0]
      if team=="KC": team="KCR"
      if team=="SD": team="SDP"
      if team=="FLA": team="MIA"
      if team=="CWS": team="CHW"
      print "%s,%s,%s,%s" % (a,team,mlb[a][2],spring[a][2])
