Recently I've been working with qmail+vpopmail+sqwebmail+courier-imap+...+a lot of things at work.
Sqwebmail has a nice code style, but unfortunally it isn't docummented at all, so for all of us that don't belong to the project itself is very painful. In addition, the way they've done some things can really piss off someone. Not to mention that it's extremely un-extensible. So adding a new feature involves understanding and modifying the whole source code.
Anyway, vacations mode is only implemented through qmailadmin, which is good, but users should use only one web interface, and that interface should be sqwebmail.

So anyways, let's cut off the story and show you some code:

<http://dcortarello.googlepages.com/sqwebmail-5.1.2-vacations-mode.patch>
