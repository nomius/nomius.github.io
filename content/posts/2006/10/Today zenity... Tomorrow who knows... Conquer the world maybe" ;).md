I was trying to make some visual scripts for Kwort Linux. I tried Xdialog but wasn't very nice. So I give a look at zenity (which I already did 2 years ago).
So the screenshots and its flexibility was amazing, there was just one thing... It needed gnome-canvas, which requiere half gnome's dependencies.
Then I started to look into the code to see if there's a way to get rid of canvas package. After few minutes I realised that canvas was only needed in about dialog; this is not a post with criticism to the zenity developers, who I think they made an excelent job with it, but add a new dependency just to draw their's about dialog wasn't the smartest thing.
I know they use it to fit the gnome's look & feel, but use canvas just for an about dialog was kind of silly, with it you only get gnome users (which unfortunally is the gnome's development idea, but I know that you guys want to do the right thing in the right way :D).

So today I wrote a patch to drop the libgnome-canvas package as dependency. Now Xfce users and everyone else not using gnome can install zenity without installing half gnome. :)

Anyways, I leave you the patch:
<http://dcortarello.googlepages.com/zenity-no-canvas.patch>
