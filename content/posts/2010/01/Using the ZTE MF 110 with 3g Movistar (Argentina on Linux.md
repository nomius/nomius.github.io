Hello all,
Today I'm going to explain how to do something really simple. As some of you might already know, I got this year a EEE PC netbook (1000HA). I have to admit that this baby is going great, I'm running the latest Kwort on it and it's really resource saving if you know how to set it up correctly.
If I add this netbook a 3g connection, I can say that I'm online everywhere almost all of the time. Well, this is what happened... As most of you already know, I've been working for Accenture for over a year now and they provided me (and some of my co-workers) a 3g modem with internet connection, which is pretty nice.
So, on january 1st after all the people who came my home to celebrate the new year left I sitted on the computer to figure out how to make it work.
This is a ZTE MF 110, and I found some people who made it work (kinda) or those who plugged it in at ubuntu and said that it works OoTB. Well, this is true kind of, but I hate when you don't really know how things works. Also, I found some people who made it parcially work with wvdial, which is a nice tool also.
So, my quest was to make it work with plain pppd. And this isn't really hard to do if you know a little how to play with the AT commands.

Ok, let's put the hands in the mud, first of all, I'm one of those people who likes to have a latest kernel tuned for my device, so this implies that yeah, I compile my own kernel with almost every release... In this case we are compiling 2.6.32.2.
So, for this you'll need the usb mass storage system in order to be able to switch from it to the modem mode.

```
Device Drivers -> USB Support -> (Select your usb version, ehci, uhci or ohci) USB Mass Storage support
```

Now, this GSM modem (as several others) needs the serial support... Well, actually, this is a serial GSM modem that you want to jack into the USB bus. So you need:

```
Device Drivers -> USB Support -> USB Serial Converter support
```

This will create the usbserial module. And now, you need the GSM modem support. So for this, you have to select:

```
Device Drivers -> USB Support -> USB Serial Converter support -> USB driver for GSM and CDMA modems
```

I would recommend you to compile them as modules (M) instead of built in, as this isn't a feature that you will be running all the time, so you can unload modules and free some memory (not too much, but everything counts nowadays).

I'm assumming that you already have the PPP support, if not, it's in the device drivers and Network Devices. But if you're reading this, you might already know.

Now, everything is ready for us to set it up.

We need [usb_modeswitch](http://www.draisberghof.de/usb_modeswitch/), this tool will allow us to switch from the "ZeroCD" mode to the modem mode in order to allow us to call our provider. Basically we need this config (/etc/usb_modeswitch.conf):

```
DefaultVendor=0x19d2
DefaultProduct=0x2000

TargetVendor=0x19d2
TargetProduct=0x0031

MessageEndpoint=0x1
MessageContent="55534243b8fe6681000000000000061b000000020000000000000000000000"
```

This config file will make the usb_modeswtich to swtich the device 0x2000, of the vendor 0x19d2, to 0x0031 sending the message pointed by MessageContent. If the usb_storage module is loaded and you run:

```
usb_modeswtich -c /etc/usb_modeswitch.conf
```

And then you run lsusb you'll see the product id changed from 2000 to 0031.

If you got here, now it comes to nice part.
In order for us to not use wvdial, we need a call script (also called chat script). I'm going to show you you the script I wrote (/etc/ppp/peers/chats/movistar):

```
ABORT BUSY ABORT 'NO CARRIER'
ABORT VOICE ABORT 'NO DIALTONE'
ABORT 'NO DIAL TONE' ABORT 'NO ANSWER'
ABORT DELAYED
'' ATZ
OK ATQ0\sV1\sE1\sS0=0\s&C1\s&D2\s+FCLASS=0
OK AT+CGDCONT=1,"IP","internet"
OK-AT-OK ATX3DT*99#
CONNECT \d\c
```

This basically it reads like this: abort in any of the conditions above (no carrier, no dialtone, etc...), then reset the modem waiting for nothing, initialize the modem, find out the CID for an APN GPRS, dial and connect. There's information about Hayes AT commands all over the web, so if you're interested you can google it yourself. :-)

Well, now we have to set up our user and password:

```
echo -e "internet\t*\tinternet" >> /etc/ppp/chap-secrets
```

And finally, the ppp configuration itself (/etc/ppp/peers/movistar):

```
lock
hide-password
noauth
connect "/usr/sbin/chat -v -f /etc/ppp/peers/chats/movistar"
/dev/ttyUSB2
460800
defaultroute
noipdefault
user "internet"
mtu 1492
ipparam movistar
```

Most of this options are self explanatory, but the importants one are the connect line and the "/dev/ttyUSB2" one. The first one tells pppd to use the chat program to connect the other point and the chat script that will be used (/etc/ppp/peers/chats/movistar, that we created before), if, for example, you set up a pptp connection you'll see this line pointing to the pptp client
program. The second one tells pppd the modem device, maybe you have to play a little bit with this one trying /dev/ttyUSB2 or /dev/ttyUSB3 (if you don't wan't to try you can use minicom to find out, good luck with that :-P).

Well, now everything is ready to connect, you just need to run:

```
pppd call movistar
```

From now one, if you restart your laptop/netbook or normal PC, all you have to do is:

```
usb_modeswitch
sleep 1  # Let the device sync with the switch
pppd call movistar
```

