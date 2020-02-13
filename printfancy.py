#!/usr/bin/env python3
##########################################################################
# A python class used for colorful and stylized printing to the command line.
#
# Author: Michael Vonbun
# Email : m.vonbun@gmail.com
#
# Sources
# The class definition is inspired from
#   https://www.geeksforgeeks.org/print-colors-python-terminal/
# 4-Bit color codes taken from
#   https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
#
# Example usage
# Calling the script from the command line shows a little demo of
# (mis)configuring the printer class.
#
# Have fun!
##########################################################################


class printFancy:
    """Basic colorized print function using ANSI codes.

    All parameters are optional.

    Class init:
      myprint = printFancy( fg='colorname',
                            bg='colorname',
                            style='style' | ['list', 'of', 'styles'],
                            end='print-end' )

    Class usage:
      myprint.pr('Text')                   : print formatted 'Text'
      myprint.avail('fg' | 'bg' | 'style') : list available colors/styles
      myprint._str('Text')                 : format 'Text' without printing it

    4-Bit color codes taken from
    https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
    """

    def __init__(self, fg=None, bg=None, style=None, end=None):
        self.fg_avail = {'black': '\033[30m',
                         'red': '\033[31m',
                         'green': '\033[32m',
                         'orange': '\033[33m',
                         'blue': '\033[34m',
                         'purple': '\033[35m',
                         'cyan': '\033[36m',
                         'lightgrey': '\033[37m',
                         'darkgrey': '\033[90m',
                         'lightred': '\033[91m',
                         'lightgreen': '\033[92m',
                         'yellow': '\033[93m',
                         'lightblue': '\033[94m',
                         'pink': '\033[95m',
                         'lightcyan': '\033[96m',
                         'white': '\033[97m'}
        self.bg_avail = {'black': '\033[40m',
                         'red': '\033[41m',
                         'green': '\033[42m',
                         'orange': '\033[43m',
                         'blue': '\033[44m',
                         'purple': '\033[45m',
                         'cyan': '\033[46m',
                         'lightgrey': '\033[47m',
                         'darkgrey': '\033[100m',
                         'lightred': '\033[101m',
                         'lightgreen': '\033[102m',
                         'yellow': '\033[103m',
                         'lightblue': '\033[104m',
                         'pink': '\033[105m',
                         'lightcyan': '\033[106m',
                         'white': '\033[107m'}
        self.reset = '\033[0m'
        self.style_avail = {'bold': '\033[01m',
                            'disable': '\033[02m',
                            'underline': '\033[04m',
                            'reverse': '\033[07m',
                            'strikethrough': '\033[09m',
                            'invisible': '\033[08m'}

        # process options
        # foreground
        if fg in self.fg_avail:
            self.fg = self.fg_avail[fg]
        else:
            if fg is not None:
                self._warning(fg, 'foreground color', 'fg', 'colors')
            self.fg = ''

        # background
        if bg in self.bg_avail:
            self.bg = self.bg_avail[bg]
        else:
            if bg is not None:
                self._warning(bg, 'background color', 'bg', 'colors')
            self.bg = ''

        # multiple styles can be provided as list
        if type(style) is list:
            valid_styles_list = []
            some_styles_valid = False
            some_styles_invalid = False
            for s in style:
                if s in self.style_avail:
                    some_styles_valid = True
                    valid_styles_list.append(self.style_avail[s])
                else:
                    some_styles_invalid = True

            if some_styles_valid is True:
                self.style = ''.join(valid_styles_list)
                if some_styles_invalid is True:
                    self._warning('found for some names',
                                  'text styles', 'style', 'styles')
            else:
                self.style = ''
                self._warning('correct at all', 'text styles',
                              'style', 'styles')
        else:
            if style in self.style_avail:
                self.style = self.style_avail[style]
            else:
                if style is not None:
                    self._warning(style, 'text style', 'style', 'styles')
                self.style = ''

        # print's line ending
        self.end = end

    # unified warning message
    def _warning(self, arg, first, second, last):
        print('Warning: No {} "{}".'.format(first, arg))
        print('See printFancy.avail("{}") for available {}.'.format(second, last))

    # low level string formatter
    def _str(self, text):
        return '{}{}{}{}{}'.format(self.fg, self.bg, self.style, text, self.reset)

    # main print interface
    def pr(self, text):
        if self.end is None:
            print('{}'.format(self._str(text)))
        else:
            print('{}'.format(self._str(text)), end=self.end)

    # option interface
    def avail(self, choice):
        info_en = False
        if choice is 'fg':
            avail_list = list(self.fg_avail.keys())
            avail_spec = 'foreground colors'
            info_en = True
            # print(len(avail_list))
            # print('{}'.format(', '.join(avail_list)))

        if choice is 'bg':
            avail_list = list(self.bg_avail.keys())
            avail_spec = 'background colors'
            info_en = True

        if choice is 'style' or choice is 'styles':
            avail_list = list(self.style_avail.keys())
            avail_spec = 'text styles'
            info_en = True

        if info_en is True:
            if len(avail_list) is 16:
                print('Available {} are\n  {}\n  {}\n  {}\n  {}'.format(
                    avail_spec,
                    ', '.join(avail_list[0:4]), ', '.join(avail_list[4:8]),
                    ', '.join(avail_list[8:12]), ', '.join(avail_list[12:])))
            if len(avail_list) is 6:
                print('Available {} are\n  {}\n  {}'.format(
                    avail_spec,
                    ', '.join(avail_list[0:3]), ', '.join(avail_list[3:])))
        else:
            print('Error:avail: Unknown option {}'.format(choice))


# demo
if __name__ == '__main__':
    print('*****************************************************')
    print('**                Print Fancy Demo                 **')
    print('*****************************************************')

    bold_pr = printFancy(style='bold')
    underline_pr = printFancy(style='underline')
    orange_pr = printFancy(fg='orange')
    purple_pr = printFancy(bg='purple')
    print('** In this demo, we want to use the class to print **\n** {} {} {} text on {} ground.   **'.format(
        bold_pr._str('bold'), underline_pr._str('underlined'), orange_pr._str('orange'), purple_pr._str('purple')))
    print('*****************************************************')
    print('')

    print('** First we try to set a foreground color that is, well nonsense:')
    print(">> myprint = printFancy(fg='nonsense')")
    myprint = printFancy(fg='nonsense')
    print('')

    print('** Next, we check the list of available color names and styles:')
    print(">> myprint.avail('fg')")
    myprint.avail('fg')
    print(">> myprint.avail('bg')")
    myprint.avail('bg')
    print(">> myprint.avail('style')")
    myprint.avail('style')
    print('')

    print('** Finally, time to do it all right:')
    print(
        ">> myprint=printFancy(fg='orange', bg='purple', style=['bold', 'underline'])")
    myprint = printFancy(fg='orange', bg='purple', style=['bold', 'underline'])
    print(">> myprint.pr('Happy printing!')")
    myprint.pr('Happy printing!')

# EOF
