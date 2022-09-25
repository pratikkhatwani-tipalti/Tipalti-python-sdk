# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 19:17:01 2022

@author: pratik.khatwani
"""
from bs4 import BeautifulSoup
def prettyXML(result):
    bs = BeautifulSoup(result,'xml')
    pretty_xml = bs.prettify()
    print(pretty_xml)