#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from conf import *
import sys, os, fnmatch, calendar, re, markdown2

def FullParse(Content):
    return markdown2.markdown(Content, extras=['fenced-code-blocks'])

class Blog:
    def __init__(self, blog_name  = 'Home'):
        self.parsed_content = ""
        self.page_counter = 0
        self.file_posts = []
        self.blog_name = blog_name

    def GetPosts(self):
        for root, dirs, files in os.walk(POSTS_LOCATION):
            for basename in files:
                if fnmatch.fnmatch(basename, '*.md'):
                    self.file_posts.append(os.path.join(root, basename))
        self.file_posts.sort(reverse=True)

    def CreateBlogPages(self):
        current_item = post_counter = 0
        self.GetPosts()
        total_items = len(self.file_posts)
        for post in self.file_posts:

            with open(post, "r") as pst:
                print "    .·-> Parsing post: " + post
                date_posted = post.replace(POSTS_LOCATION, '').split('/')
                self.parsed_content += "<h3>" + os.path.splitext(os.path.basename(post))[0] + "</h3>"
                self.parsed_content += "<h6>Posted on: " + calendar.month_abbr[int(date_posted[2])] + ' ' + date_posted[1] + "</h6>"
                self.parsed_content += FullParse(pst.read())
                self.parsed_content += '\n' + BLOG_POST_SEPARATOR + '\n'
                post_counter += 1
                current_item += 1

            # Change the page
            if post_counter == POSTS_PER_PAGE:
                if current_item + 1 == total_items:
                    page_counter = self.WriteBlogPage(True)
                else:
                    page_counter = self.WriteBlogPage(False)
                post_counter = 0
                self.parsed_content = ""

        if post_counter != 0:
            self.WriteBlogPage(True)

    def WriteBlogPage(self, bottom):
        if INDEX_AS_BLOG:
            fstr = 'index'
        else:
            fstr = 'blog'

        if self.page_counter == 0:
            fname = fstr + '.html'
            if not bottom:
                pprev = '<a href="' + fstr + str(self.page_counter + 1) + '.html">Previous posts</a>'
            pnext = ''
        else:
            fname = fstr + str(self.page_counter) + '.html'
            if self.page_counter == 1:
                pnext = '<a href="' + fstr + '.html">Next posts</a>'
            else:
                pnext = '<a href="' + fstr + str(self.page_counter - 1) + '.html">Next posts</a>'
            if not bottom:
                pprev = '<a href="' + fstr + str(self.page_counter + 1) + '.html">Previous posts</a>'
            else:
                pprev = ''
        prev_next = '<table style="width:100%"><tr><td>' + pprev + '</td><td align="right">' + pnext + '</td></tr></table><br>'

        with open(fname, 'w') as page_file:
            print '   Writing file: ' + fname
            pw = Writters(page_file, '<br><br>' + self.parsed_content)
            pw.WriteHTMLHead()
            pw.WriteNavBar(self.blog_name)
            pw.WriteMainContent(content_is_filename = False)
            pw.WriteFooter(prev_next)
        self.page_counter += 1

class Writters:
    def __init__(self, file_output, content):
        self.file_output = file_output
        self.content = content

    def WriteHTMLHead(self):
        csss = ""
        try:
            for css in ADDITIONAL_CSS:
                csss += '<link href="' + css + '" rel="stylesheet">'
        except:
            pass
        with open (TEMPLATE_LOCATION + '/head.html', "r") as tf:
            self.file_output.write(tf.read().replace('%TITLE%', TITLE).replace('%MORE_CSS%', csss))

    def WriteMainContent(self, content_is_filename = True):
        if content_is_filename:
            with open (CONTENT_LOCATION + '/' + self.content + '.md', "r") as cf:
                o_content = cf.read()
                parsed_content = FullParse(o_content)
        else:
            parsed_content = self.content
        with open (TEMPLATE_LOCATION + '/content.html', "r") as tf:
                self.file_output.write(tf.read().replace('%CONTENT%', parsed_content))

    def WriteFooter(self, footext = ""):
        with open (TEMPLATE_LOCATION + '/footer.html', "r") as tf:
            self.file_output.write(tf.read().replace('%FOOTER%', footext))

    def WriteNavBar(self, active):
        navbar = ""
        for item in NAVBAR:
            if type(item) is str:
                name = item.split('|')[0]
                link = item.split('|')[1]
                if link == 'blog' and INDEX_AS_BLOG:
                    link = 'index.html'
                elif link == 'blog':
                    link = 'blog.html'
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
        with open (TEMPLATE_LOCATION + '/navbar.html', "r") as tf:
            self.file_output.write(tf.read().replace('%TITLE%', TITLE).replace('%NAVBAR_ITEMS%', navbar))


def Page(name, fname):
    with open(fname, 'w') as page_file:
        pw = Writters(page_file, name)
        pw.WriteHTMLHead()
        pw.WriteNavBar(name)
        pw.WriteMainContent(content_is_filename = True)
        pw.WriteFooter()


def main(argv):
    for item in NAVBAR:
        if type(item) is str:
            name = item.split('|')[0]
            outfname = item.split('|')[1]
            cfile = CONTENT_LOCATION + '/' + name + '.md'
            if outfname == 'blog':
                print "Creating a weblog in: " + name
                b = Blog(name).CreateBlogPages()
            elif os.path.isfile(cfile):
                Page(name, outfname)
                print "Generating: " + outfname
        elif type(item) is list:
            for iitem in item[1]:
                name = iitem.split('|')[0]
                outfname = iitem.split('|')[1]
                cfile = CONTENT_LOCATION + '/' + name + '.md'
                if os.path.isfile(cfile):
                    print "Generating: " + outfname
                    Page(name, outfname)

if __name__ == "__main__":
    main(sys.argv)
