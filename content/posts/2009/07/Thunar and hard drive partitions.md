Hello everybody, It's been so long since my last post here.
There's so much to talk about, but today I'm going to talk about Thunar. As some of you might know, thunar is the file manager used in Xfce, written by Benedikt Meurer, and nowadays maintained by Jannis Pohlmann.
I really like thunar, but the fact that hard drive partitions are left to the distribution itself when hal can manage them and because of that the file manager also can, isn't really nice, as you can browse your partitions in newer versions of GTK's (with Gvfs) GtkFileChooser.
An ugly workaround would be to mount them and add some gtk bookmarks, but you would like to set an emblem to differentiate them from normal bookmarks, and emblems are not part of the gtk library, so you wouldn't see emblems in a GtkFileChooser. Another issue would be that isn't dynamic, so if someone change partitions that would be a total mess.
So IMHO the best solution to this is: Hard Drive partitions managed by hal (DeviceKit in the future) and let Thunar show them in the left pane. And this is what I actually did.

So, as everybody loves screenshots and you probably want to see how this looks:

![Thunar and partitions](http://1.bp.blogspot.com/_7bn3_3YdSWU/SlohSHN0aCI/AAAAAAAAAPs/uRExbB-PPIk/s400/thunar_hd_partitions.png)

And finally, the patch: <http://dcortarello.googlepages.com/Thunar-1.0.0-hd-partitions.diff>

Enjoy!
