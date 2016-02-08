#!/bin/python

import argparse
import json
import re
import os
from time import time
import datetime
import time

parser = argparse.ArgumentParser(description='Convert to Quiver Format')
parser.add_argument("src", help="The Source File You want to Convert")
args = parser.parse_args()

def gtime(x):
    return time.mktime(datetime.datetime.strptime(x,'%Y%m%d%H%M%f').timetuple())

with open(args.src) as f:
    tids = json.load(f)

notebookpath = "tiddly.qvnotebook"
if not os.path.exists(notebookpath): os.makedirs(notebookpath)

meta = {
    "name": "TiddlyWiki",
    "uuid": "Tiddly"
}

with open(notebookpath + "/meta.json", 'wb') as f:
    json.dump(meta, f)

for i, tid in enumerate(tids):
    text = tid['text']
    text = re.sub("^#", "*   ", text, flags=re.M)
    text = re.sub("^!!!", "###", text, flags=re.M)
    text = re.sub("^!!", "##", text, flags=re.M)
    text = re.sub("^!", "#", text, flags=re.M)
    text = re.sub("{{{", "```", text, flags=re.M)
    text = re.sub("}}}", "```", text, flags=re.M)
    text = re.sub("\\\\\\[", "$$", text, flags=re.M)
    text = re.sub("\\\\\\]", "$$", text, flags=re.M)
    text = re.sub("//", "*", text, flags=re.M)

    cells = []
    cells.append({
        "type": "markdown",
        "data": text,
            })
    content = {"title": tid['title'], "cells": cells}

    if not tid.has_key('modified'):
        modified = tid['created']
    else:
        modified = tid['modified']

    if not tid.has_key('tags'):
        tags = []
    else:
        tags = [tid['tags']]

    meta = {
        "tags" : tags,
        "title" : tid['title'],
        "created_at" : int(gtime(tid['created'])),
        "updated_at" : int(gtime(modified))
    }

    notepath = "tiddly.qvnotebook/note-%05d.qvnote" % (i)
    if not os.path.exists(notepath): os.makedirs(notepath)

    with open(notepath + "/content.json", 'wb') as f:
        json.dump(content, f)

    with open(notepath + "/meta.json", 'wb') as f:
        json.dump(meta, f)
