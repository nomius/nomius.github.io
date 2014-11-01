Ok, ok, ok... I know I was in vacations, but the day wasn't very pretty, and I felt like taking a coding time. :D

Some weeks ago I wrote a small plugin for Xfce to configure the network in Kwort Linux; I was going to use Zenity, but then I saw again Xdialog and surprise... GTK2 based interface!

Well... Nowadays a program which keeps being maintained using gtk1 is something very weird. So I decided to use Xdialog. The problem was when I needed an extra button... Dialog provides that feature, but Xdialog didn't and I really needed it.

So I mailed Thierry Godefroy asking him if he didn't had a patch which provides that feature... I guess he was very, very occupied, because he didn't even answered.

When I saw the code the first time some weeks ago I said "This will be hard to understand to implement it by myself", and today when I started to look at the code it wasn't that hard. So some hours latter I understanded the code and started to write some things...

So, this is what this command:

```bash
Xdialog --stdout --extra-button --extra-label "Extra Button" --inputbox "Type your input. Hit Extra Button to get 3 as return value" 0 0
```

will show:

![Xdialog extra button](http://photos1.blogger.com/blogger2/288/3652/400/xdialog-button-extra-patch.png)

So... Here's the patch, I hope someone finds it useful like me:

(http://dcortarello.googlepages.com/Xdialog-2.3.1-patch-extra-button.patch)
