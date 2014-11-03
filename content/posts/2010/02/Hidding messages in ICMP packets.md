Hello everybody. A new month, a new article (I wish I could do this so periodically).

Today I'm going to show you something that I've been playing with. As you probably know (if you don't, I'm just telling you now :-)), the ICMP packets provides an arbitrary data space right after the ICMP header. Normally, no one use it, since ICMP is a control protocol that has all its usage right inside of it, leaving this data space useless.

A few days ago, I saw someone connected on Cinetix and he was just connected, but not on the IRC server and I didn't know who he or she was. So an idea started to flow around my head "What about if I could send messages with ICMP packets".

So actually this is what I did... I wrote a tool to put a message in the data space and send it using the ICMP type 7 which is unassigned (for example, ping is the type 8). The problem is that the kernel just drop type 7 (as we all assume) and the data space is also dropped in any icmp packet. So I wrote a kernel patch that print the message in the output of dmesg or
/var/log/message if you have set KERN_NOTICE to be displayed (I think klogd -c 6 does).

With this, you can send to a friend a message of the kind "Hey. This is David, I'm online on irc (jabber or whatever), jump in!" and it will be displayed in the system logs as a kernel notice.

Please, take note that this is not a chat system, but an "emergency system", so don't start using it as an everyday conversation protocol. This also isn't a patch that should be in the kernel mainstream, since ICMP packets of type 7 is unassigned, and NOT a communication protocol.

##### What about security?
Well, you might start asking yourself this "What if someone from the outside starts flooding my logs with dumb messages?". Right, well, the answer to this is netfilter; use iptables to drop these kind of package. Something like this:

```
iptables -A INPUT -p icmp --icmp-type 7 -j DROP
```
As you might know or guess, you can also block only one IP address or accept from a certain network like this:

```
iptables -A INPUT -p icmp --icmp-type 7 \! -s 10.0.0.1/24 -j DROP
```
Use more complex rules creating policies like "if someone exceed the number of 5 ICMP type 7 packets in a minute, drop any packet from the IP address".

##### Enough with the talking... How do I use it?
Great, right to the point. So the steps:

1. First of all, patch and compile your kernel.

```
cd linux-2.6.31 && patch -p1 < patch_icmp_type_7_messages.diff
```
And compile and install your new kernel using the way you normally do (make config/menuconfig, etc...)

2. Then compile the icmp\_send.c program:

```
gcc icmp_send.c -o icmp_send
```
3. Send a test message:

```
./icmp_send 127.0.0.1 "Hello world"
```
4. Check out the dmesg output:

```
./dmesg | grep "ICMP 7 Message"
```

Get it!
Anyways, this is a really nice thing to play with and I hope people find it useful. You can get the kernel patch and the ICMP message program from the links below.

[patch\_icmp\_type\_7\_messages.diff](http://nomius.github.io/content/patches/patch_icmp_type_7_messages.diff)

[icmp\_send.c](http://nomius.github.io/content/patches/icmp_send.c)

Have fun.

