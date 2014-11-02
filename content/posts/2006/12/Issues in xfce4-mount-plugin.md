I planed to add xfce4-mount-plugin to Kwort's panel, but there was some things to fix and to change.

The first patch fixes some issues with some file systems which shouldn't be shown, like tmpfs and root partition. I mean, those shouldn't be displayed, since the users should not mount or umount it.

<http://dcortarello.googlepages.com/xfce4-mount-plugin-0.4.7-noroot-notmpfs.patch>

This patch is for the same plugin, but is just for behavior. It just make the plugin to not display the device block since the user is not interested on it but where the data will be displayed.

<http://dcortarello.googlepages.com/xfce4-mount-plugin-0.4.7-no-block-device.patch>

I mailed Jean Baptiste Dulong to change it, but he's not maintaining the plugin anymore, so who knows who should I send the patch. :P

