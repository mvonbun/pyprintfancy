# python-print-fancy
Print color- and stylized text in Python3.

## Usage

After importing the module, instantiate the `fancyPrint` class with options.
Calling the module from the command line gives a small demo on the usage.

## Class Interface
```
Class init:
  myprint = fancyPrint( fg='colorname',
                         bg='colorname',
                         style='style' | ['list', 'of', 'styles'],
                         end='print-end' )
Class usage:
  myprint.pr('Text')                   : print formatted 'Text'
  myprint.avail('fg' | 'bg' | 'style') : list available colors/styles
  myprint._str('Text')                 : format 'Text' without printing it
```

## Class Demo

``` shell
>> ./print-fancy.py
*****************************************************
**           print-fancy.fancyPrint Demo           **
*****************************************************
** In this demo, we want to use the class to print **
** bold underlined orange text on purple ground.   **
*****************************************************

** First we try to set a foreground color that is, well nonsense:
>> myprint = fancyPrint(fg='nonsense')
Warning: No foreground color "nonsense".
See fancyPrint.avail("fg") for available colors.

** Next, we check the list of available color names and styles:
>> myprint.avail('fg')
Available foreground colors are
  cyan, blue, yellow, black
  lightblue, white, lightcyan, lightgrey
  lightred, lightgreen, darkgrey, red
  pink, orange, green, purple
>> myprint.avail('bg')
Available background colors are
  cyan, blue, yellow, black
  lightblue, white, lightcyan, lightgrey
  lightred, lightgreen, darkgrey, red
  pink, orange, green, purple
>> myprint.avail('style')
Available text styles are
  reverse, underline, invisible
  bold, strikethrough, disable

** Finally, time to do it all right:
>> myprint=fancyPrint(fg='orange', bg='purple', style=['bold', 'underline'])
>> myprint.pr('Happy printing!')
Happy printing!
```

