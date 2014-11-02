This issue came up today with some people and I did affirmed that you can hang up your switch with some funny code...
How this come? Well, very simple, switches and bridges has a small stack (10 bytes per host connected to it) where they save IP and MAC addresses to know where to send a package once the sender and the receiver are known. So, once the first package is sent, a new entry in the stack was made. So now you know the "theory" I'll leave you to think how could this help you to hang it
(Let me give you a hint: OVERFLOW).

Anyways, get the code you'll need to produce this overflow from here: <http://dcortarello.googlepages.com/pkinject>

Keep in mind that you'll need the pktgen kernel module to run this.
See also that I did this 3 years ago with bash, not even C code, so it shows how easy is to generate network packages to produce this effect, which isn't a big deal when it comes to reproduce it, but to create a security policy to avoid it.

Have fun.

