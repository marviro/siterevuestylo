from flask import Flask, render_template, redirect, send_file 
import tools
import config
import pypandoc
import re
import makecaches
import json
import os
from slugify import slugify



app = Flask(__name__, template_folder='./templates/')

if config.dynamic:
    print('dynamic version')
else:
    print('version with caches')
    makecaches.makecaches()

article = tools.idfrommyid("01-recom")
# print(article)
data = tools.testAuthors(article)
formatted = tools.formatnameslinks(data)
print(f"data: {data} \n formatted: {formatted}")


# print(data)