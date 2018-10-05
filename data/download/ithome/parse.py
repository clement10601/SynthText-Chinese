# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 mrg <mrg@MrG-MacBook-Pro>
#
# Distributed under terms of the MIT license.

"""

"""
import re 
import os
import codecs
import shutil
import glob
import re
from bs4 import BeautifulSoup, Comment

regex = r'[<!].*.[\*\/]'

txtdir = 'output_txt'
if not os.path.isdir(txtdir):
    os.makedirs(txtdir)
for html in glob.glob("output/*.html"):

    base = os.path.basename(html)
    name, ext = os.path.splitext(base)
    outputFile = open(os.path.join(txtdir, name + ".txt"), "w")

    with open(html, "r") as f:
        t = f.read()

        soup = BeautifulSoup(t, "html.parser")


        for p in soup.find_all("h1", class_="page-header"):
            if p.get_text().strip() != "":
                outputFile.write(p.get_text().strip() + "\n")

        content_block = soup.find_all("p")[:-13]
        text = [''.join(s.findAll(text=True))for s in content_block]
        nt = []

        for t in text:
            res = re.search(regex, t, re.MULTILINE)
            if res:
                continue
            if t != "":
                outputFile.write(t + "\n")

        for p in soup.find_all("div", class_="views-field views-field-title"):
            if p.get_text().strip() != "":
                outputFile.write(p.get_text().strip() + "\n")

        outputFile.close()

    #print "-----------------------------------------------------------------------------------------------------------"
