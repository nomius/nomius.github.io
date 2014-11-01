Well, a friend of mine asked me for this, and it was very interesting to understand what was in /proc/net/dev.

```bash
#!/usr/bin/env bash

if [ -z "${1}" ]; then
   echo "Give a network interface"
   exit 1
fi
DEV=${1}
/sbin/ifconfig ${DEV} >/dev/null 2>&1
if [ $? -ne 0 ]; then
   echo "Please, do man 8 ifconfig to know what a network interface is"
   exit 1
fi
LINE_OLD=$(cat /proc/net/dev | grep ${DEV})
sleep 1
LINE_NEW=$(cat /proc/net/dev | grep ${DEV})
while [ "${LINE_OLD}" = "${LINE_NEW}" ]; do
   sleep 0.1
   LINE_NEW=$(cat /proc/net/dev | grep ${DEV})
done
OLD_DOWN=$(echo ${LINE_OLD/*:/} | awk -F " " '{ print $1 }')
OLD_UP=$(echo ${LINE_OLD/*:/} | awk -F " " '{ print $9 }')
NEW_DOWN=$(echo ${LINE_NEW/*:/} | awk -F " " '{ print $1 }')
NEW_UP=$(echo ${LINE_NEW/*:/} | awk -F " " '{ print $9 }')
REST_DOWN=$((${NEW_DOWN} - ${OLD_DOWN}))
REST_UP=$((${NEW_UP} - ${OLD_UP}))
if [ ${REST_DOWN} -gt 1024 ]; then
   echo "DOWNLOAD: $(echo "scale=2;${REST_DOWN}/1024" | bc -lq)k/s"
else
   echo "DOWNLOAD: ${REST_DOWN}b/s"
fi
if [ ${REST_UP} -gt 1024 ]; then
   echo "UPLOAD: $(echo "scale=2;${REST_UP}/1024" | bc -lq)k/s"
else
   echo "UPLOAD: ${REST_UP}b/s"
fi
```

You can run it this way for example:

```bash
while true; do ./netspeed eth0; done
```

I don't think this is really reliable, but anyways, see you guys in the next few days to tell you something new :)

