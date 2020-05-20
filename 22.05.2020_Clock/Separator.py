class Separator:

    symbol = '\u2593'
    line = 9

    def __init__(self, separator):
        if separator == 0:
            self.list_sep = ['   {0}{0}   '.format(self.symbol),
                             '        ',
                             '        ',
                             '        ',
                             '        ',
                             '        ',
                             '        ',
                             '        ',
                             '        ']
        if separator == 1:
            self.list_sep = ['        ',
                             '        ',
                             '        ',
                             '        ',
                             '   {0}{0}   '.format(self.symbol),
                             '        ',
                             '        ',
                             '        ',
                             '        ']
        if separator == 2:
            self.list_sep = ['        ',
                             '        ',
                             '        ',
                             '        ',
                             '        ',
                             '        ',
                             '        ',
                             '        ',
                             '   {0}{0}   '.format(self.symbol)]
                
    def get_line(self, counter):
        return self.list_sep[counter]
