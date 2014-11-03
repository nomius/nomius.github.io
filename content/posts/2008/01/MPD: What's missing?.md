I been using mpd+gmpc now for a while, I really like the combination, but what I missed on it was the ability to modify tags, which normally all players can do.
Well, I started working on gmpc to add support for tag editing when I stopped with the following issue: The fact that mpd doesn't support tag editing was the reason for gmpc to not support it (which makes sense), because mpd is run on a different machine so gmpc does not have access to these files.
Some of you will tell me "Dude! Sonata supports tag editing even when mpd doesn't", and I know, but what sonata does is actually a very like a "half done work" with that, as you can only edit tags if mpd runs on the same machine sonata is running, which normally doesn't happen (that's the idea of a client-server structure).
So, now, my approach to resolve the problem was completely different as I had to include a new command in the mpd protocol so I could add tag editing support.
Well, I did include the command, I did gave support to tag edition and I even gave a command to check if the file can be edited or not. Finally, I gave support to libmpd and gmpc, so now, gmpc can "full edit" tags. :-)

So here are the patches (descriptions on how to use the commads can be found in mpd's patch, and descriptions on how to use the new functions libraries can be found in libmpd's patch):
MPD (stable version, by now 0.13.0): [mpd-0.13.0-tag_edit_support.patch](http://nomius.github.io/content/patches/mpd-0.13.0-tag_edit_support.patch)

LIBMPD (stable version, by now 0.15.0): [libmpd-0.15.0-tag_edit_support.patch](http://nomius.github.io/content/patches/libmpd-0.15.0-tag_edit_support.patch)

GMPC (stable version, by now 0.15.0): [gmpc-0.15.5.0-tag_edit_support.patch](http://nomius.github.io/content/patches/gmpc-0.15.5.0-tag_edit_support.patch)

Now, the main problem wasn't the code itself, I mean, I had to spend some time investigating the code to finally hint the right keys. But the problem is now in what mpd developers want to do with this patch. Some developers like it (specially client's developers and users, like Qball Cow and Scott Horowitz), but others disagree. I really understand both sides (I have to admit I
like more mine's, that's why I developed this patch).
Some argues that the patch will add more code to maintain, but actually, the mpd's patch is not more than 300 lines (so that excuse looks more like a joke), others say that mpd is just a music player with a client-server architecture, and not a tag editing software, and I really understand this philosophy. But IMHO I think that if mpd wants to take care of the music this is
like "a must have".

Since this made very people a little uncomfortably, I see this like something good, not because of the internal fight/war, but because it helps to discuss the development. The fact that is being considered means the project is still alive and defining issues while the time is going on.
People say that if this doesn't get in trunk tag editing is off the table. Well guys, if that happens, bad luck.

Anyways, Kwort 2.4 will use mpd+libmpd+gmpc with tag editing support. :-)
