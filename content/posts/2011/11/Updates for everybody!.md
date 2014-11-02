I'm a disaster to write a blog, sorry for the delay.
There have been lot of news in the past few months. Let's enumerate one by one:
I created a small project called mttools, and this is basically a set of tools to write good technical documentation, with formated code inside and some pretty nice features. The nice thing about this tools is that it forced me to learn Unix flex :-)
You can check out this project at: <http://code.google.com/p/mttools>

As some of you might have noted, Kwort 3.2 got released, this is a pretty clean and nice release that got some really nice features and improvements. If you like Kwort > 3, please, step by <http://www.kwort.org>, read the announcement and try it.
There's also some nice new features and bug fixes in kpkg, that were deployed with Kwort 3.2, if you're not using Kwort but you're using kpkg, you should step by <http://code.google.com/p/kpkg>

One of the cool stuff that came up with Kwort 3.2 are the ports; we are now supporting the crux ports, that you can bring to your system by:

```
  kpkg install httpup rsync fakeroot rsync ports
```

I'll blog a little on the CRUX ports latter on.

Also there's a new release of ktsuss, just baked. This release has some bug fixes in the su backend and guess what... There's a sudo backend now too!
You should get the release at <http://code.google.com/p/ktsuss>.

NOTE: 1.4 code has critical bugs and is completely unmaintained, so please update to the latest release. I also removed all extra repositories like the one at berlios, github, etc, so there's now only one at google code avoiding confussions.

The last few months I worked a little on LimShSQL and there's a full new re-write with a pretty shinny curses interface in limshsql-rewrite-1.0 branch, I think I should merge it soon and package a release. Check it out here: <http://code.google.com/p/limshsql>

