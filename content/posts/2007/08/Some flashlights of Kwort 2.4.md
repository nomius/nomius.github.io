Well, me and the rest of the team are working in Kwort 2.4 (2.2.2? I dunno, but I think 2.4 will be alright).

Andreas Schipplock (aka Avaurus) is working on the core system and as far as I know he is making a remarkable work on it.
One of the most important parts is the lzma compression for the packages, so the final iso will be smaller than the Kwort 2.2 one. He is now working on the installation system, so when he gets done I'll put Kwort desktop on it.

Stijn Segers is working on the new interface for the users admin system (as my mockup looked very bad :-P), so once he finishes with it I will make a Xfce plugin of it and include it in the mcs settings manager.
He will also take care of the kernel. So this time, getting kernel source to compile drivers won't be needed and as he told me we will include some drivers by default like those free ralink ones. But kernel work stopped until 2.6.23 come out, as that one will be the one for Kwort 2.4.

And it's time to tell what I'm doing... Well, until Andreas and Stijn doesn't finish I'm still maintaining 2.2 serie including and upgrading packages (http://www.kwort.org/?page=MorePackages).
But until that happens I'm checking projects and taking decisions for the desktop and in core (helping Andreas and Stijn). Today I did some user custom actions for kwort packages:

![Installing Kwort packages from the file manager](https://sites.google.com/site/dcortarello/kpkg_install.png)

For those paranoids (I know you guys are right about this), ktsuss will be included and all those sudo commands will be removed (sudo will still be included, but not used for anything else but xfsm-shutdown-helper). So this custom action showed above use ktsuss in case you ask.


Oh, another interesting things are the fact that kwort is listed in www.xfce.org/download/distros as a Xfce distribution and Kwort being used in school (COBAEH - Cuautepec de Hinojosa - Hidalgo - Mexico) with old machines (Pentium MMX 200Mhz with 32MB ram).

Well, that's all for now folks, I will keep bringing Kwort newsflash :)
