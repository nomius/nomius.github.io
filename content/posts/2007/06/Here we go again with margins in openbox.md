I wrote a patch for openbox 3.3.1 at the very beginning of the year which was rejected by the openbox leader (to me the reasons wasn't right, but it is his project :-P).
So a new release of openbox was released some weeks ago and yes, as you guess, that patch isn't compatible with the new version (3.4), so I re-wrote the patch to work.

The configuration is made in the same way as before in the rc.xml:

```xml
<margin>
  <top>px</top>
  <bottom>px</bottom>
  <left>px</left>
  <right>px</right>
</margin>
```

So, here it is, patch supporting margins in openbox 3.4: (http://dcortarello.googlepages.com/openbox-3.4.0-margins.patch)

Thanks to all the people asking me for this, as it inspiring.

