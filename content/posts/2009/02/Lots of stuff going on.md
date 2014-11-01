Well, it's been 3 months since my last post, and I've been doing a lot...

Let's start with Kwort. Well we're just there from the release, lots of new improvements are being done around it, and something really interesting is the new network manager and the new user manager I wrote from scratch with a completely new design using gtkdialog.

The new network manager allows you to configure your ethernet and wireless network, supporting static and dhcp, for wireless network, support for several encryption mode are available, from wep to wpa2:

![Network manager](http://lh3.ggpht.com/_7bn3_3YdSWU/SZCvNk3odHI/AAAAAAAAANM/6m-TJD-_8Cw/knm.png)

The user manager stills very simple but with a very simple and smooth interface:

![User manager](http://lh5.ggpht.com/_7bn3_3YdSWU/SZCvNl6KKtI/AAAAAAAAANU/Q7Lh7X_hYTA/kum.png)

So, as you can see we have almost everything, since looking at the screenshot the Xfce settings manager is in it, so Xfce is kinda there, so you might be questioning "What are you waiting for a release?" Well, Xfce 4.6 is in release candidate time, so when they release it final we'll see how's the Mozilla people going with Firefox 3.1, since it would be really cool to ship it
with Kwort 2.4.1. I wouldn't matter to ship a beta 3 with 2.4.1, but we'll see, since beta 3 should be released already according to [Mozilla's Firefox schedule](https://wiki.mozilla.org/Firefox3.1/Schedule), and their delivery meeting is schedule to the end of the month (February 25th), which is just around the corner.

Resuming, lots of improvements are going on and I'm trying to make it pretty cool and easy for the end user.

That's just for Kwort, now... Some friends saw I was migrating to git, and yeah, I did, since in the past I used git with [gitorious.org](http://www.gitorious.org/) which didn't convinced me, I came back to darcs. But now, I discovered [GitHub](https://www.github.com/) which is really cool, fast and easy to use and with lots of guides around, so you can see and follow my work
at: (http://github.com/nomius).
I have to admit here that I was influenced at work by warlock, which is the author of the [wbar](http://www.warlockshome.com.ar/), to move from darcs to git, so I found a darcs2git python script and it was like charm.

Also, I implemented lots of cool new features for kpkg, and I merged kpkg with the kwort network manager and user manager making a "big" project called [kwtools](http://github.com/nomius/kwtools/tree/master). Looking right now at the master tree page, you'll see this: "Implemented kpkg search /all with csv support" and you might be asking "What the hell is this guy making with kpkg implementing stuff like this?", well, I hope this feature is just enough, but basically, it is because a friend, x-ip, and I we are writing a graphical interface for kpkg, at the moment the interface is pretty rough but does show the idea, of course, icons and all that stuff is going to be implemented with also a more eye-candy interface, so you can see a preview of the application here:

![kpkg graphical](http://lh5.ggpht.com/_7bn3_3YdSWU/SZCvNhGOhsI/AAAAAAAAANc/SV4rvaIufCg/galgo.png)

As I said before and as you can see, the interface looks pretty rough, but give us some time and you'll see how cool it looks. I doubt we get in time to include this new tool in Kwort 2.4.1, we'll try, but I really doubt it since I'm just learning python, which is the language we use to write this, and x-ip is just learning wxPython with me, which is the framework we use for
this.

Please, if you have any ideas for Kwort or any of the tools/applications I write, please write me, it would be nice to hear (read) about you and your ideas, and also, I don't know... help maybe? :-)

We'll, this post is already becoming large so I'm off to bed now. Have a nice week and see you around guys.
