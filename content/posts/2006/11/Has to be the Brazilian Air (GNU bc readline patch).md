The same day I wrote the patch for Xdialog's extra button feature (when I was in Rio de Janeiro - Brazil) I found a little bug in the GNU bc using readline.
The bug actually is very simple, there was a wrong prototype declaration of the extern function readline. The prompt argument, according to readline(3) from GNU, is a const char *, not a char *.
So bc didn't even compile if you wanted to use readline (which actually is very good). I must think that eveyone uses bc without readline, so nobody saw that error.
Anyways, I wrote the patch and send it to Phil Nelson (author of GNU bc), and he thank me for it.

I don't know when bc is gonna be updated so I don't know either when the patch will be included. So, for now, you'll have to download it from here and apply it manually.

(http://dcortarello.googlepages.com/bc-1.06-readline-const-char.patch)

