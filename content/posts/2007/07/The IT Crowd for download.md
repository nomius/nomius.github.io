The last week I started to see a tv serie called "The IT Crowd" on Sony, it's a funny geek serie about an IT team in a british company. Anyways, a friend of mine (Manu) wanted to download all the chapters from a site, so I wrote this simple script for him:

```bash
#!/usr/bin/env bash

wget http://stage6.divx.com/The-IT-Crowd---Spanish-Subtitled/videos/
i=1
for x in $(egrep -i "The-IT-Crowd---1x0*" index.html | awk -F '/' '{ print $4}' | sort -m -u); do
   tput setaf 1
   echo "Downloading chapter ${i} (Link: http://divx-226.vo.llnwd.net/stage6vid/${x}.divx)"
   tput sgr0
   wget http://divx-226.vo.llnwd.net/stage6vid/${x}.divx --output-file="${i}.avi"
   i=$((i+1))
done
```

I hope someone find it useful.

EDIT: Unfortunately, this doesn't work anymore, since stage6 was closed.

