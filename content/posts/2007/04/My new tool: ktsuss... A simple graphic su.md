I know I had to write something about the wake on lan software I was writing. I think it is done, but couldn't test it yet, so I don't wanna rush me and write about it and show it in case it doesn't work, so please stay tunned and wait a bit longer.

So, today I will show and talk you about a new thing I was doing these days.
I started working on a replacement for gksu. gksu is like a graphical su. I was trying to understand it and make it work well enough, but I don't know what was in the mind of the gksu's developers, because what they did was a really wrong approach, I don't know why they wrote first a library and then the application (maybe for plugins, I'm just paraphrasing) , but anyways,
together they are more than 500k, which is extremely too much.
So I wrote my version of gksu, which is called ktsuss (keep the su simple, stupid). My version is only the setuid wrapper (as GTK doesn't permit setuid programs) and program itself which is less than 3k.
As I know you guys love screenshots, this is how the program looks like:

![ktsuss 1.0 screenshow](http://1.bp.blogspot.com/_7bn3_3YdSWU/RirMWAa4iZI/AAAAAAAAAE0/bjUfY8bq2Ek/s320/ktsuss.png)

Anyways, I would like to get feedback on this, so please, let me know if it fails or anything is or goes wrong on it.

Get the program from here: <http://dcortarello.googlepages.com/ktsuss-1.0.tar.gz>
