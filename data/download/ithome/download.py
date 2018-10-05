# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright Â© 2018 mrg <mrg@MrG-MacBook-Pro>
#
# Distributed under terms of the MIT license.

"""

"""
import os
import codecs
import requests

typeList = ["news", "buying", "tech", "feature", "big-data", "cloud", "devops", "security"]
#for t in typeList:
if not os.path.isdir("output"):
    os.makedirs("output")

for t in typeList:
    for idx in range(8441, 130000, 1):
        fp = "output/{}_{}.html".format(t, idx)
        if os.path.exists(fp):
            continue
        print("https://www.ithome.com.tw/{}/{}".format(t, idx))
        with open(fp, 'w') as f:
            a = requests.get("https://www.ithome.com.tw/{}/{}".format(t, idx)).text
            f.write(a)
