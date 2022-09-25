"""
Created on Fri Sep 23 17:57:01 2022

@author: pratik.khatwani
"""


def extractResponse(response):
    s=str(response)
    start=">"
    end="<"
    return s[s.find(start)+len(start):s.rfind(end)]

