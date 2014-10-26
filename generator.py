#!/usr/bin/env python

from conf import *
import sys
import gfm

def FullParse(Content):
    return gfm.markdown(Content)

def WriteHTMLHead():
    with open ("templates/head.html", "r") as tf:
        print tf.read().replace('%TITLE%', TITLE)


def WriteMainContent(content):
    with open ("content/" + content + '.md', "r") as cf:
        o_content = cf.read()
        parsed_content = FullParse(o_content)

    with open ("templates/content.html", "r") as tf:
            print tf.read().replace('%CONTENT%', parsed_content)


def WriteFooter():
    with open ("templates/footer.html", "r") as tf:
        print tf.read().replace('%TITLE%', TITLE)


def WriteNavBar(active):
    navbar = ""
    for item in NAVBAR:
        if type(item) is str:
            name = item.split('|')[0]
            link = item.split('|')[1]
            if name == active:
                navbar += '<li class="active"><a href="' + link + '">' + name + '</a></li>\n'
            else:
                navbar += '<li><a href="' + link + '">' + name + '</a></li>\n'
        elif type(item) is list:
            navbar += '<li class="dropdown">\n<a href="#" class="dropdown-toggle" data-toggle="dropdown">' + item[0] + '<span class="caret"></span></a>\n<ul class="dropdown-menu" role="menu">\n'
            for iitem in item[1]:
                name = iitem.split('|')[0]
                link = iitem.split('|')[1]
                navbar += '<li><a href="' + link + '">' + name + '</a></li>\n'
            navbar += '</ul></li>\n'

    with open ("templates/navbar.html", "r") as tf:
        print tf.read().replace('%MENU_TITLE%', MENU_TITLE).replace('%NAVBAR_ITEMS%', navbar)

WriteHTMLHead()

if len(sys.argv) > 1:
    WriteNavBar(sys.argv[1])
else:
    WriteNavBar('Home')

if len(sys.argv) > 1:
    WriteMainContent(sys.argv[1])

WriteFooter()
