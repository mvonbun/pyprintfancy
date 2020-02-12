# PYPRINTFANCY
Print color- and stylized text in Python3.

## Installation
From your local copy

``` shell
git pull https://github.com/mvonbun/pyprintfancy.git
cd pyprintfancy
python3 -m pip install --user printfancy-mvonbun
```
or

``` shell
git pull https://github.com/mvonbun/pyprintfancy.git
cd pyprintfancy
python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
```

## Usage

After importing the module, instantiate the `fancyPrint` class with options.  An
example from `ipython3`:

``` python
In [1]: import pyprintfancy.printFancy as prfancy

In [2]: myprint = prfancy.fancyPrint(fg='orange', bg='purple', style=['bold', 'underline'])

In [3]: myprint.pr('yay')
yay

```


Calling the module from the command line gives a small demo on the **usage**

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


## Class Interface
```
Class init:
  myprint = prfancy.fancyPrint( 
	  fg='colorname',
      bg='colorname',
      style='style' | ['list', 'of', 'styles'],
      end='print-end' )
Class usage:
  myprint.pr('Text')                   : print formatted 'Text'
  myprint.avail('fg' | 'bg' | 'style') : list available colors/styles
  myprint._str('Text')                 : format 'Text' without printing it
```


## Sources
The class definition is inspired from
[https://www.geeksforgeeks.org/print-colors-python-terminal/](https://www.geeksforgeeks.org/print-colors-python-terminal/)

The 4-Bit color codes are taken from
[https://en.wikipedia.org/wiki/ANSI_escape_code#Colors](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors)
