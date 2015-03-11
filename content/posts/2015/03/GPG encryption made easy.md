So as I said before I started to play more with GPG and made some really quick bash functions to encrypt and decrypt data. Here we go:

Encrypt:

```sh
encrypt()
{
    if [ -e "${1}.crypt" ]; then
        tput setaf 1
        echo "* ERROR * ${1}.crypt already exists. Exiting..."
        tput sgr0
        return 1
    fi

    i=0
    while read line; do
    items+=("$i" "$line")
        i=$(($i + 1))
    done < <(gpg --list-keys | grep @ | sed -e 's/uid[ ]*\[.*\] //g')
    i=$(LC_ALL=en_US dialog --stdout --backtitle "Encryption made easy" \
        --title Encrypt --menu "Pick the recipient" $(($i + 7)) 76 $i "${items[@]}")
    if [ $? -ne 0 ]; then
        return 0
    fi
    recp=$(echo "${items[$(($i + 1))]}" | awk -F '[<>]' '{print $(NF-1)}')

    gpg --output "${1}.crypt" --encrypt --recipient ${recp} "${1}"
}
```

Decrypt:

```sh
decrypt()
{
    out=$(basename "$1" .crypt)
    if [ "${out}" = "$1" ]; then
        out=$(LC_ALL=en_US dialog --stdout --backtitle "Encryption made easy" \
            --title Decrypt --inputbox "Type the output filename" 8 40)
        if [ $? -ne 0 -o -z "$out" ]; then
            return 0
        fi
    fi
    gpg --output "${out}" --decrypt "${1}"
}
```
