import colorama

colorama.init()
class Number:

    symbol = '\u2593'
    line = 9

    def __init__(self, number):
        if number == 0:
            self.list_number = ['{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol)]
        if number == 1:
            self.list_number = ['{0}{0}{0}{0}{0}   '.format(self.symbol),
                                '   {0}{0}   '.format(self.symbol),
                                '   {0}{0}   '.format(self.symbol),
                                '   {0}{0}   '.format(self.symbol),
                                '   {0}{0}   '.format(self.symbol),
                                '   {0}{0}   '.format(self.symbol),
                                '   {0}{0}   '.format(self.symbol),
                                '   {0}{0}   '.format(self.symbol),
                                '{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol)]
        if number == 2:
            self.list_number = ['{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol),
                                '{0}{0}      '.format(self.symbol),
                                '{0}{0}      '.format(self.symbol),
                                '{0}{0}      '.format(self.symbol),
                                '{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol)]
        if number == 3:
            self.list_number = ['{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol)]
        if number == 4:
            self.list_number = ['{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol)]
        if number == 5:
            self.list_number = ['{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol),
                                '{0}{0}      '.format(self.symbol),
                                '{0}{0}      '.format(self.symbol),
                                '{0}{0}      '.format(self.symbol),
                                '{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol)]
        if number == 6:
            self.list_number = ['{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol),
                                '{0}{0}      '.format(self.symbol),
                                '{0}{0}      '.format(self.symbol),
                                '{0}{0}      '.format(self.symbol),
                                '{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol)]
        if number == 7:
            self.list_number = ['{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol),
                                '{0}{0}      '.format(self.symbol),
                                '{0}{0}      '.format(self.symbol),
                                '{0}{0}      '.format(self.symbol),
                                '{0}{0}      '.format(self.symbol)]
        if number == 8:
            self.list_number = ['{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol)]
        if number == 9:
            self.list_number = ['{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}    {0}{0}'.format(self.symbol),
                                '{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '      {0}{0}'.format(self.symbol),
                                '{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.symbol)]
        if number == 10:
            self.list_number = ['        ',
                                '        ',
                                '        ',
                                '   {0}{0}   '.format(self.symbol),
                                '        ',
                                '   {0}{0}   '.format(self.symbol),
                                '        ',
                                '        ',
                                '        ']
        
    def get_line(self, counter):
        return self.list_number[counter]
