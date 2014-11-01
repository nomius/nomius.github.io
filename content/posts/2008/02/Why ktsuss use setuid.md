Well, this was the question made by one of the debian packagers. I see a good thing the fact that they ask this, since including a program setuid without asking the reasons would be kind of dumb. They ask why not using pam or su in the way gksu does, so I will try to answer these questions.

Using pam would requiere setuid too (since pam_unix2 doesn't have it's own wrapper), which doesn't bother me as long as I program in a secure way... What really does, is that not every distribution out there use pam, slackware is the most important it comes to my mind now.
Using su, well, there might be a problem there, gksu does it in a very unportable way waiting for the string " Authentication failure" which is a very bad idea, look this example:

```
Fedora "su" command:
-sh-3.1$ su
Password:
su: incorrect password
-sh-3.1$
Slackware (Kwort) "su" command:
nomius@Neptune:~$ su
Password:
Sorry.
nomius@Neptune:~$
```

As you can see in gksu, different versions of su would really break things up.
None of above shown implementations gives " Authentication failure". I guess that message is given by pam with strerror(), so once again, it's not portable.

The actual ktsuss code is very clean and simple (which is the whole idea behind ktsuss), I always gave security with the authentication backend, maybe a feature bug (like the PATH thing in 1.1), but not security issues.

There might be a way using su better than what gksu does, something like doing "su -c exit" (pepping the password of course) getting the exit status with WEXITSTATUS(), waiting for 0 (password ok and then run su command with the same password) or 1 (wrong password). But would be kind of messy...
I should see that like something in a long distant future... But I think it could be a way to avoid the paranoid.

So since ktsuss have its own implementation of authentication backend, that's why it needs setuid.
