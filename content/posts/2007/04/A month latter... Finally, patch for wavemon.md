It's been quite a while since my last post here...

Some things happened like the release of Kwort 2.2 (not as great as I would like, but still good). New knm will be released in the next few days, this will be just a bug fix release (too many thanks to the people from tuxmachines, who thanks to them I saw some bugs).

I've been developing on clip at work, which is an interesting and exciting thing, since this is my first time working on compilers (I started last year when I wrote some patches for compatibilities and bug fixes).

Well, now on to businesses and the important stuff. As I said like a month ago I was working on a patch for wavemon, which is a software that I consider very good, with a nice and clean code. I would have released it before, but I was studying and working a lot, so I only have the weekends, and as I been working on Kwort I couldn't work on this before.

So, as it says in the patch, the following bug fixes and features:

* Fixed errors compilation in gcc 3.x due to default label missing.

* Fixed some warnings due to the lvalue casts deprecated on gcc 3.x.

* Changed ap list functions, so now it use the new iw api (this is the most important thing).

The last change is the most important, as it made the code simpler, now it works with all cards because the new wireless tools extensions are up to date.

Get the patch from here: <http://nomius.github.io/content/patches/wavemon-0.4.0b-comp-fix-new-ap.patch>

And for those that don't know wavemon, you can get the source code from here: <http://www.janmorgenstern.de/wavemon-current.tar.gz>

I hope you guys find it useful like I do. :)
