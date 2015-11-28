# -*- coding:utf-8 -*-
import requests
import urllib2

s = requests.session()
url = "http://uzone.univs.cn/verifyimage.webpage.jpg"
w = urllib2.urlopen(url)
print w.read()
