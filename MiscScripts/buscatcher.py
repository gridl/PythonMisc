#!/usr/bin/env python3
import sys
import urllib.request
from xml.etree.ElementTree import  XML


if len(sys.argv) != 3:
    raise SystemExit("Usage: buscatcher.py route stopID")
route = sys.argv[1]
stopID = sys.argv[2]

u = urllib.request.urlopen("http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stopI={}".format(route,stopID))
data =u.read()
print(data)
doc = XML(data)
for pt in doc.findall('.//pt'):
    print(pt.text)