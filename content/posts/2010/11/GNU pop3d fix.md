Wooooo, kinda a lot without saying something here! Well, I took some sabbatical months of blogging ;-) 

Recently I've been working on a mail server, and those who know me, knows that I'm pretty minimalistic. So I started with exim and gnu-pop3d (no imap for this) with stunnel to provide ssl support.
I use Unix users for authentication, but gnu-pop3d had a (pretty small) bug which made it reject any authentication whether it is right or wrong.
So I wrote a patch to provide a fix and sent it to Jorgen Thomsen. He answered me on Wednesday telling me that the patch was accepted.

Anyways, I leave the patch here: [gnu-pop3d-0.9.12-fix_passwd_login.patch](https://sites.google.com/site/dcortarello/gnu-pop3d-0.9.12-fix_passwd_login.patch)

Cheers!
