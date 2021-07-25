import cmd
from view import *
import tigrExtend as tIgr
from drawer import *


class CommandLine(cmd.Cmd):

    def __init__(self, src_reader):
        cmd.Cmd.__init__(self)
        self.source_reader = src_reader
        self.parser = self.source_reader.parser
        self.drawer = self.source_reader.parser.drawer
        self.source = []
        self.prompt = '(tigr cmd):'
        self.file = None
        self.command_list = {}
        self.intro = 'Welcome to the tigr cmd.   Type help or ? to list commands.\n'

    def do_pendown(self, arg):
        """Will put the pen down, enabling drawing"""
        data = 'D'
        self.parse(data)
        self.source.clear()

    def do_draw(self, data):
        """ Draw a line:
            [N or NORTH] : Moving to north direction
            [E or EAST] : Moving to east direction
            [S or SOUTH] : Moving to south direction
            [W or WEST] : Moving to west direction
            [NE or NORTH-EAST] : Moving to NorthEast direction
            [SE or SOUTH-EAST] : Moving to south-east direction
            [SW or SOUTH-WEST] : Moving to south-west direction
            [NW or NORTH-WEST] : Moving to north-west direction"""
        self.parse(data)
        self.source.clear()

    def do_penup(self, arg):
        """ Will put the pen up, disabling drawing"""
        data = 'U'
        self.parse(data)
        self.source.clear()

    def do_pensize(self, pen_size):
        """Sets the width of the pen. -> pensize <size> """
        data = f'P {pen_size}'
        self.parse(data)
        self.source.clear()

    @staticmethod
    def do_bye(arg):
        """Exit from the application, closing.... ->  bye"""
        print('Thank you for using tigr command line interface')
        exit()
        return True

    def do_record(self, switch_input):
        """Save future commands to filename  ->  record [-start] [filename]
        To Stop recording command process ->  record [-stop] """
        source = switch_input.split()
        file = ''
        try:
            switch = source[0]
            if len(source) > 1:
                for index in range(1, len(source)):
                    i = source[index]
                    if i != '':
                        file = i
            if switch.lower() == '-start':
                try:
                    self.file = open(file, 'w')
                    print(f'Recording the commands in {file}')
                except FileNotFoundError as err:
                    if file == '':
                        print('Please specify the file name to record the command')
                    else:
                        print(f'{err}')
            elif switch.lower() == '-stop':
                self.close()
                print('Stopping from recording command')
            else:
                print(f'Syntax error. Usage: record [-start][filename] / record [-stop]')
        except IndexError:
            print(f'Syntax error. Usage: record [-start][filename]\nrecord [-stop]')

    def do_parse_file(self, arg):
        """Read and executes commands from a file ->  parse_file [filename]"""
        self.close()
        try:
            with open(arg) as f:
                self.cmdqueue.extend(f.read().splitlines())
        except FileNotFoundError:
            if arg == '':
                print('Please specify the file name to read')
            else:
                print(f'File [{arg}] is not found')

    def precmd(self, line):
        line = line.lower()
        if self.file and 'parse_file' not in line:
            print(line, file=self.file)
        return line

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    def parse(self, data):
        commands = data.split(',')
        for command in commands:
            self.source.append(command)
        self.source_reader.parser.parse(self.source)


if __name__ == '__main__':
    drawer = TurtleDrawer()
    myParser = tIgr.MyParser(drawer)
    the_src_reader = tIgr.MySourceReader(TheView, myParser)
    cli = CommandLine(the_src_reader)
    cli.cmdloop()

