Well, I don't know how many are actually reading this, maybe none, but anyways, here we go...

So Kwort 4.3.3 is almost out and here's some highlights to share:

* Everything is up to date as you expect, toolchain, kernel (latest 4.14 LTS -as of now 4.14.32-).
* A small kpkg bug has been fixed (this was actually *discovered* by the latest gcc version).
* Chromium 65 is our default browser now. 
* We dropped Firefox as they don't support alsa anymore as sound backend. Additionally Firefox now requires Rust so that would require another almost 200MBs in the ISO. But, we know our userbase is pretty conscious about privacy and we also know that Firefox goes pretty much together with that aspect when it comes to a full featured browser, so for the `browser` command, Firefox is the desired option if it's installed by the user, otherwise it falls back into chromium and then chrome. As said before: bear in mind that you'll need rust in order to run any recent version of Firefox.
* LLVM is now included in the standard installation. Why LLVM and no Rust? Well, the rational behind the green light for LLVM is that mesa3d (gallium specifically) requires llvm to support radeon. Additionally, but this is secondary, Chromium now uses llvm (clang specifically) to build. This is one of those things which I hate (having two tools for the same (llvm & gcc)), I really hope things get more aligned in the future and one of those can be dropped, but I don't see that happening (at least not in the short term).
* We are dropping flash support. The option is still available in Chromium, but we are not distributing the ppapi object anymore,
* New UI themes using our standard tools (openbox, GTK2 and GTK3).

If people is looking on running Google Chrome instead of Chromium, a script named `chrome_packaging.sh` is available in the ISO in boot/tools that will package Google Chrome from the latest version available (this one requires libcups available in the repository).
Additionally, if you need kernel headers, a script named `gen-kernel-headers-tarball.sh` is available in the ISO in boot/tools. I would advice you to run it against the kernel version distributed by Kwort, as normally kernel headers needed are the same used when compiled the libc.

Where to download the first release candidate? [kwort-4.3.3rc1.iso](http://kwort.org/downloads/kwort-4.3.3rc1.iso) [md5sum](http://kwort.org/downloads/kwort-4.3.3rc1.iso.md5) [sha1sum](http://kwort.org/downloads/kwort-4.3.3rc1.iso.sha1)

Cheers!
