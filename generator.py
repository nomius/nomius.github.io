#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from conf import *
import sys, os, fnmatch, datetime, re, markdown2

link_patternss = [
    #(re.compile(r"[(.*)]([A-Za-z0-9]*://.*)", re.I), r"<a href=\"\2\">\1</a>"),
    #(re.compile(r"([A-Za-z0-9]*://.*)", re.I), r"\1")
]

def FullParse(Content):
    return markdown2.markdown(Content, extras=['fenced-code-blocks', 'link-patterns'], link_patterns=link_patternss)


def WriteBlogPage(page_counter, template, parsed_content, bottom):
    if INDEX_AS_BLOG:
        fstr = 'index'
    else:
        fstr = 'blog'

    if page_counter == 0:
        out = fstr + '.html'
        if not bottom:
            pprev = '<a href="' + fstr + str(page_counter + 1) + '.html">Previous posts</a>'
        pnext = ''
    else:
        out = fstr + str(page_counter) + '.html'
        if page_counter == 1:
            pnext = '<a href="' + fstr + '.html">Next posts</a>'
        else:
            pnext = '<a href="' + fstr + str(page_counter - 1) + '.html">Next posts</a>'
        if not bottom:
            pprev = '<a href="' + fstr + str(page_counter + 1) + '.html">Previous posts</a>'
        else:
            pprev = ''
    prev_next = '<table style="width:100%"><tr><td>' + pprev + '</td><td align="right">' + pnext + '</td></tr></table>'

    with open(out, "w") as fout:
        print 'Writing file: ' + out
        WriteHTMLHead(fout)
        WriteNavBar(fout, 'Home')
        fout.write(template.replace('%CONTENT%', '<p>' + parsed_content))
        WriteFooter(fout, prev_next)
        fout.close()
    return (page_counter + 1)


def CreateBlog():
    fposts = []
    for root, dirs, files in os.walk('content/posts'):
        for basename in files:
            if fnmatch.fnmatch(basename, '*.md'):
                fposts.append(os.path.join(root, basename))
    fposts.sort(reverse=True)
    with open ("templates/blog.html", "r") as tf:
        txt_template = tf.read()

    post_counter = page_counter = 0
    parsed_content = ""

    current_item = 0
    total_items = len(fposts)
    for post in fposts:

        with open(post, "r") as pst:
            print " '-> Parsing post: " + post
            parsed_content += "<h3>" + os.path.splitext(os.path.basename(post))[0] + "</h3>"
            parsed_content += "<h8>Posted on: " + datetime.datetime.fromtimestamp(os.path.getmtime(post)).strftime("%Y-%m-%d %H:%M:%S") + "</h8>"
            parsed_content += FullParse(pst.read())
            parsed_content += '\n<hr width="40%">\n'
            post_counter += 1
            current_item += 1

        # Change the page
        if post_counter == POSTS_PER_PAGE:
            if current_item + 1 == total_items:
                page_counter = WriteBlogPage(page_counter, txt_template, parsed_content, True)
            else:
                page_counter = WriteBlogPage(page_counter, txt_template, parsed_content, False)
            post_counter = 0
            parsed_content = ""

    if post_counter != 0:
        WriteBlogPage(page_counter, txt_template, parsed_content, True)


def WriteHTMLHead(f):
    with open ("templates/head.html", "r") as tf:
        f.write(tf.read().replace('%TITLE%', TITLE))


def WriteMainContent(f, content):
    with open ("content/" + content + '.md', "r") as cf:
        o_content = cf.read()
        parsed_content = FullParse(o_content)

    with open ("templates/content.html", "r") as tf:
            f.write(tf.read().replace('%CONTENT%', parsed_content))


def WriteFooter(f, footext):
    with open ("templates/footer.html", "r") as tf:
        f.write(tf.read().replace('%FOOTER%', footext))


def WriteNavBar(f, active):
    navbar = ""
    for item in NAVBAR:
        if type(item) is str:
            name = item.split('|')[0]
            link = item.split('|')[1]
            if link == 'blog' and INDEX_AS_BLOG:
                link = 'index.html'
            if name == active:
                navbar += '<li class="active"><a href="' + link + '">' + name + '</a></li>\n'
            else:
                navbar += '<li><a href="' + link + '">' + name + '</a></li>\n'
        elif type(item) is list:
            navbar += '<li class="dropdown">\n<a href="#" class="dropdown-toggle" data-toggle="dropdown">' + item[0] + '<span class="caret"></span></a>\n<ul class="dropdown-menu" role="menu">\n'
            for iitem in item[1]:
                name = iitem.split('|')[0]
                link = iitem.split('|')[1]
                if link == 'blog' and INDEX_AS_BLOG:
                    link = 'index.html'
                navbar += '<li><a href="' + link + '">' + name + '</a></li>\n'
            navbar += '</ul></li>\n'

    with open ("templates/navbar.html", "r") as tf:
        f.write(tf.read().replace('%TITLE%', TITLE).replace('%NAVBAR_ITEMS%', navbar))


def CreatePage(name, fname):
    with open(fname, 'w') as f:
        WriteHTMLHead(f)
        WriteNavBar(f, name)
        WriteMainContent(f, name)
        WriteFooter(f, "")


def main():
    for item in NAVBAR:
        if type(item) is str:
            name = item.split('|')[0]
            outfname = item.split('|')[1]
            cfile = 'content/' + name + '.md'
            if outfname == 'blog':
                CreateBlog()
            elif os.path.isfile(cfile):
                print "Generating: " + outfname
                CreatePage(name, outfname)
        elif type(item) is list:
            for iitem in item[1]:
                name = iitem.split('|')[0]
                outfname = iitem.split('|')[1]
                cfile = 'content/' + name + '.md'
                if os.path.isfile(cfile):
                    CreatePage(name, outfname)
                    print "Generating: " + outfname

main()

