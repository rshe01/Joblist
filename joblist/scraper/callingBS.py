# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 16:06:58 2021

@author: richa
"""
from .bs import bs

def big():
    arr = []
    for x in range(3):
        arr.append(bs("https://www.indeed.com/jobs?q=Computer+Science+Internship&start="+str(x*10)))
    return arr
