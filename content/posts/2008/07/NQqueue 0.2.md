Well, I just tagged NQqueue as 0.2. Several changes has been done from 0.1. For those who doesn't know, NQqueue is a threaded queue for qmail with support for plugins. Full details of what nqqueue is can be found here: <http://nomius.blogspot.com/2008/06/nqqueue-what-is-that.html>

Download the latest release version here: <http://europa.fapyd.unr.edu.ar/releases/NQqueue-0.2.tar.gz>

Changelog can be found here: <http://europa.fapyd.unr.edu.ar/darcs/NQqueue/Changelog>
If you want to get nightly builds packages. Use this link: <http://europa.fapyd.unr.edu.ar/darcs/NQqueue/NQqueue.tar.gz>
Darcs repository: <http://europa.fapyd.unr.edu.ar/darcs/NQqueue>

NQqueue stills in development, it is stable enough, but there are some things that must be fixed before the next release.

Plugins included:

1. General plugins:
   * black - Parameters:
     * user@domain - email address to put in the blacklist.

   * clamav - Parameters:
     * "pass" - will make the email pass even if it contains a virus (used to send it to a quarantine).
     * None parameter given will block a containing virus mail.

2. User plugins:
   * dspam - Parameters:
     * "pass" - will make the email pass even if it considered spam (used to send it to a quarantine).
     * None parameter given will block a spam considered email.

   * quarantine - Parameters:
     * "all" - will send to quarantine any email that was considered spam or that contains a virus.
     * "dspam" will send to quarantine any email that was considered spam.
     * "clamav" - will send to quarantine any email that contains a virus.
     * "q=" - allow the administrator to set the quarantine type. Allowed types of quarantines are:
       * general - will put the email in /var/qmail/nqqueue/quarantine.
       * vquad(VHOME) - will put the email in your vpopmail home (ex: vquad(.Spam), will put your email in Maildir/.Spam/cur). [vpopmail support must be given in configure script]

Example of common usage:
This example shown here will block an incoming email from billgates@microsoft.com, put emails containing virus to general quarantine (in /var/qmail/nqqueue/quarantine/domain/user), and deliver spam considered emails in Maildir/.Spam/new (which is the personal user spam directory in his vpopmail home).

 * /var/qmail/control/general.cfb

```
:clamav=pass;black=billgates@microsoft.com
```

* /var/qmail/control/mydomain.com.cfb

```
dspam=pass;quarantine=clamav,q=general;quarantine=dspam,q=vquad(.Spam)
```

I hope people start using nqqueue, since it is fast, secure, flexible and very easy to use.
