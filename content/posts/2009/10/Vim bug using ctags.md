Well, lot of people know that I'm a vim fan and that I use it everyday, to me is like the killer app that everyone should know how to use in Unix.
Even at work, I'm a programmer (doing C on Unix now), and some of my fellows were using Eclipse and after I show them Vim, they was like "woooo, I can use this editor as an IDE and still can use my machine for do something else while programming" (I was like, blame the one who introduced you to Eclipse :-P).

Anyways, I like using tags, allows me to browse the code really fast (for those using Eclipse, I think is like if you press F3 over a function name). But I found this weird behavior using ctags+vim. See the above code:

```c
  1 #include <stdio.h>
  2
  3 int asd(int s,
  4         char a);
  5
  6 int main(int argc, char *argv[])
  7 {
  8     asd(1, 's');
  9     return 0;
 10 }
 11
 12 int asd(int s,
 13         char a)
 14 {
 15     return s;
 16 }
```

When I press ctrl+] over asd in line 8, it takes you to the 3rd line instead to the 12th...
There's a "workaround" to this behavior, using --excmd=number while running ctags put the line numbers in the tags file (without this option ctags puts just an 'f' identifier to tell the editor that it is on that file). But it is just a visualization workaround, because you can't put any new line (or remove) in those files or your tags file will screw the tags file.

Does anyone knows a solution to this issue?

Thanks.
