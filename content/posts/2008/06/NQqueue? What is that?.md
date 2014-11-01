As some people asked me the last few weeks what I've been doing I've decided to take some time to write this and explain what NQqueue (aka nqq) is all about.
Well, some of you maybe listened (or read) me telling that queues for qmail are bloated. We don't have several choices, there is just plain qmail-queue which is unfeatured, qmail-scanner (aka give me my CPU back) which is the bloatest one, and simscan which is kind of featured, fast, but not extensible at all, both of the last ones are buggy when getting an email with several
Rcpts (they only analyze one. Which is a big bug).
So, because of all this, I've been using simscan, I actually extended it from those 2000 lines to 4000 adding features. But it became so big, that it is hard to maintain and to trace errors in it.
This situation drove me nuts the last year so I decided "Why I don't just write my own qmail queue?". Well, NQqueue is the result of this self asked question.

Let me show you and tell you some of the features of NQq:

* Modular - not like simscan with a big file with all the problem.
* Pluggable - this is what NQq is all about, it support the addition of plugins. There are some now in the darcs server.
* Threaded - this is quite a nice feature for mails with several Rcpts, nqqueue triggers a thread for every Rcpt to be analyzed.
* Fast - This is like simscan. But it improves it when analyzing more than one Rcpt because of the threads.
* Secure and reliable - I been working quite a lot on this, since simscan has several bugs, and I didn't want this on NQq.

Plugins: Well, some of you might be asking "Dude, nice, but how do I write a plugin for NQq?". Well, first of all, I have to tell you that there are two types of plugins:
1st. we have the general plugins. Those plugins are run to an email before to trigger all the threads for every rcpt. Why is this? Well, it would be dumb to call for example a clamav plugin for every user (in every thread). So for example we can write a plugin that should not care about the Rcpts and/or From, like clamav, since it depends on a general database.
2nd. besides of general plugins, there are also per user plugins. These plugins are run in every thread. This is the example of a spam plugin, since it depends on a special per user database.

So now I can show you a small general plugin to block a Sender:

```c
/* vim: set sw=4 sts=4 : */

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <nqqueue.h>

#define PLUGIN_VERSION "1.0"
#define PLUGIN_NAME "black"
#define REJECTED_MESSAGE "Message rejected because of black list"

char *plugin_name()
{
    return strdup(PLUGIN_NAME);
}

char *plugin_version()
{
    return strdup(PLUGIN_VERSION);
}

/* Parameters:
 * params = a char pointer with parameters used to call the module (in this case, the email address to block).
 * mail = It's a char pointer to the filename that contains the email.
 * From = a char pointer with the From email address. (if it matchs the param, the mail would be blocked)
 * Rcpt = an union that contains space for a char pointer (if user pluing) or a pointer to a PUStruct
 *        struct (if general plugin).
 * general = a pointer to a RSStruct struct, which is structure with all the plugins and its return values
 *           already runned by general plugins
 * peruser = a pointer to a RSStruct struct, which is structure with all the plugins and its return values
 *           already runned by per user plugins
 */
struct ModReturn *plugin_init(char *params, const char *mail, const char *From, const union Tos Rcpt, \
                              struct RSStruct *general, struct RSStruct *peruser)
{
    struct ModReturn *ret = malloc(sizeof(struct ModReturn));

    ret->NewFile = NULL;
    if (!strcmp(params, From)) {
        ret->ret = 1;
        ret->rejected = 1;
        ret->message = strdup(REJECTED_MESSAGE);
    }
    else {
        ret->ret = 0;
        ret->rejected = 0;
        ret->message = NULL;
    }
    return ret;
}
```

Looks easy don't you think? So, how do we make NQqueue to load our plugin? Simple: in /var/qmail/control/general.cfb put a line like this:

```
:black=billgates@microsoft.com
```

That will set the sender billgates@microsoft.com as a blocked server. In fact, this plugin acts just like a black list.
Now your question might be: And how can I block more? Well, you can call the plugin several times, like this:

```
:black=billgates@microsoft.com;black=steveballmer@microsoft.com
```

Or you can modify the plugin_init function to allow more than one email (like black=billgates@microsoft.com,steveballmer@microsoft.com) and do some simple parsing with strtok.


As you can see it is very easy to write plugins for NQqueue. I know it stills need a lot of documentation, since at it is now, it's very poor in this aspect. The only documentation in NQqueue so far is a configuration scheme in the NQqueue darcs in case you want to know how to configure it right (it's very easy).

So, those are some of the features in NQqueue there are more of course, but those are enough to mention.
NQqueue needs a lot of testing, so I'm counting with all of you to run tests. Also documentation is needed, and it will take some time to me to write it, so people wanting to write documentation are welcome. Also people writing plugins, I wrote some which are already in my darcs server (a dspam, clamav, blacklist and quarantine) modules.

You can follow NQqueue's development in my darcs server at: (http://europa.fapyd.unr.edu.ar/cgi-bin/darcsweb.cgi)
