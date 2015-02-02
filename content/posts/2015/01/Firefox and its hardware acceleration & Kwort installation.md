Well... So I had this feeling of going back 100% to Firefox and while doing some testing, WebGL is really bad. It looks like the problem is that the hardware acceleration sucks entirely in Firefox.
Hardware acceleration in Firefox is really a hell, even with OMTC I couldn't get more than 13 FPS, while on Chromium I get at least 60FPS using a [Firefox acceleration stress test](https://developer.mozilla.org/media/uploads/demos/p/a/paulrouget/8bfba7f0b6c62d877a2b82dd5e10931e/hacksmozillaorg-achi_1334270447_demo_package/HWACCEL/)

I've tried with an ATI R600 card, an Intel HD 4600, a Nvidia GT-740M all of them with the latest drivers that perform just great on other applications (glxsphere, chromium, etc...), I never got a decent performance, and this is the latest version of Firefox (35.0). So I guess I should just give up.
So probably on 4.2 Firefox will not be included in the ISO and only Chromium, we'll see what happens.

On other news, I've discovered several failures on the Kwort installer, and I appologize for that. I guess I should try to be "less-mainstream" and more hardcore, pretty much like the OpenBSD installation. Andreas was working on a new installer that I think he started some years ago (https://github.com/schipplock/kwort-installer-ng) but I honestly don't know... There's too much to handle nowadays and things have gotten too complicated to support everything "automatically".

For those who wants to know, Kwort's installation can be sumarized in the following list:

* Keyboard configuration
* Partitioning (cfdisk)
* SWAP, mountpoints and formating (mkswap, mkfs.\* mount in /mnt/install and all mountpoints internally)
* Package decompressing (tar + xz + sqlite, which could be all simplified with kpkg)
* Post configuration (write: fstab, rc.conf, set root password and install lilo/grub)

My future approach would probably be that we could leave most of that to the user, specially with all the fuzz of UEFI, GPT and so on.

Time will tell. :-)
