I wrote this simple script to find public samba shared resources. Windows by default leave some "open resources" that normally you can access mounting it or with some samba tools. So, the thing is: How do I find public resources in a network? This is what I did:

```sh
#!/usr/bin/env bash

function scan(){
   SUBNET=${1}
   LAST=${2}
   PING="$(which ping) -c 1 -W 1"
   ${PING} ${SUBNET}.${LAST} > /dev/null 2>&1
   if [ $? -eq 0 ]; then
       SMBRESOURCES=$(smbclient -N -L ${SUBNET}.${LAST} 2>/dev/null | grep Disk | grep -v \\$)
       if [ ! -z "${SMBRESOURCES}" ]; then
           tput setaf 2
           echo -e "Public samba resources in ${SUBNET}.${LAST}:"
           tput setaf 1
           echo "${SMBRESOURCES}"
           echo -e "------------------------------------------------------\n"
           tput sgr0
       else
           tput setaf 3
           echo "${SUBNET}.${LAST} is up, but doesn't have public resources"
           echo -e "------------------------------------------------------\n"
           tput sgr0
       fi
   fi
}

if [ -z ${2} ]; then
  for((x=1;x<255;x++)); do
      ${0} ${1} ${x} &
  done
else
  scan ${1} ${2}
fi
wait

#EOF
```
