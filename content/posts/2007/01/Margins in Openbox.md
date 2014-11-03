Last month I started using openbox to create an easy to use desktop for programmers. Everything was nice, but I wanted to use yabb with adesklets, and then ipager... Everything was nice when I launched those applications/applets, but when I maximize a window, it was over the applet.
There are some applets where that is ok, like the weather applet, but that wasn't right for a panel (like yabb) or a pager like ipager (this last one should set struts).
The solution was margins, Xfwm4 has it and other several wm (like metacity and sawfish) has it too. So I wrote a small patch to give to openbox margins.
I was very happy with it, and gave it to other users to try it (thanks gregf in irc://irc.oftc.net/slackware who tested it for a while, and who stills using it), so I made the submition in openbox's bugzilla. But guess what... The patch was rejected, and the bugzilla entry closed and deleted.
The answer of the developer was:
It's up to the pager/panel to set properties called struts. Openbox properly
respects those and doesn't maximize over them.

Which is great... I mean... Follow standards, that's good... But applets does not set struts, and sometimes the users just wants margins.
So anyways, the patch is here for everyone who wants to use it. Just has to apply it and set the margins in the configuration file like this:

```xml
<margin>
    <top>px</top>
    <bottom>px</bottom>
    <left>px</left>
    <right>px</right>
</margin>
```

So here's the patch: <http://nomius.github.io/content/patches/openbox-3.3.1-margins.patch>
