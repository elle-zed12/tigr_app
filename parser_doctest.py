
import json
from drawer import *


class MyParser:
    """
    >>> my_drawer = TurtleDrawer()
    >>> my_parser = MyParser(my_drawer)
    >>> my_parser.source.append('North 90')
    >>> my_parser.parse(my_parser.source)
    drawing line of length 90 at 0 direction
    >>> my_parser.source.clear()
    >>> my_parser.source.append('South 10')
    >>> my_parser.source.append('East 10')
    >>> my_parser.source.append('West 50')
    >>> my_parser.source.append('North 10')
    >>> my_parser.parse(my_parser.source)
    drawing line of length 10 at 180 direction
    drawing line of length 10 at 90 direction
    drawing line of length 50 at 270 direction
    drawing line of length 10 at 0 direction
    >>> my_parser.source.clear()
    >>> my_parser.source.append('S 10')
    >>> my_parser.source.append('E 10')
    >>> my_parser.source.append('W 50')
    >>> my_parser.source.append('N 10')
    >>> my_parser.parse(my_parser.source)
    drawing line of length 10 at 180 direction
    drawing line of length 10 at 90 direction
    drawing line of length 50 at 270 direction
    drawing line of length 10 at 0 direction
    >>> my_parser.source.clear()
    >>> my_parser.source.append('SE 10')
    >>> my_parser.source.append('NW 10')
    >>> my_parser.source.append('NE 50')
    >>> my_parser.source.append('SW 10')
    >>> my_parser.parse(my_parser.source)
    drawing line of length 10 at 135 direction
    drawing line of length 10 at 315 direction
    drawing line of length 50 at 45 direction
    drawing line of length 10 at 225 direction
    >>> my_parser.source.clear()
    >>> my_parser.source.append('pensize 8')
    >>> my_parser.parse(my_parser.source)
    Pen size is set to 8
    >>> my_parser.source.append('penup')
    >>> my_parser.source.append('north 100')
    >>> my_parser.parse(my_parser.source)
    Pen size is set to 8
    Pen is up! Unable to draw
    >>> my_parser.source.append('pendown')
    >>> my_parser.parse(my_parser.source)
    Pen size is set to 8
    Pen is up! Unable to draw
    Pen is down! You may start drawing
    >>> my_parser.source.clear()
    >>> my_parser.source.append('Pensize 190')
    >>> my_parser.parse(my_parser.source)
    Limit the pen size from 1 to 100. Set the pensize again
    """

    def __init__(self, the_drawer):
        super().__init__()
        # This will allow MyParser to user any drawer that follows the drawer Interface
        self.drawer = the_drawer
        self.source = []
        self.command = ""
        self.data = 0
        self.list_of_commands = {}
        self.load_command_list()
        self.is_pen_down = True
        self.message = ''

    def parse(self, raw_source):
        self.source = raw_source
        for line in self.source:
            line = line.strip()
            command_seq = line.split(" ")
            self.command = command_seq[0]
            if len(command_seq) > 1 and command_seq[1].isdigit():
                self.data = int(command_seq[1])
            elif len(command_seq) > 1 and not command_seq[1].isdigit():
                self.message = f'Not a valid value, please enter a valid [direction] [distance]'
                print(self.message)
                return
            self.what_command(self.command)

    """Loading the list of commands from a configurable json file"""

    def load_command_list(self):
        try:
            f = open("command.json")
            data = json.loads(f.read())
            for i in data['commandsList']:
                self.add_command(self.list_of_commands, i['shortcutKey'], [i["commandName"], i["description"],
                                                                           i["direction"]])
            f.close()
        except FileNotFoundError:
            print('File is not found')

    """Append multiple values to a key in the dictionary"""
    @staticmethod
    def add_command(the_dict, key, list_of_values):
        if key not in the_dict:
            the_dict[key] = list()
        the_dict[key].extend(list_of_values)
        return the_dict

    """Formatting for printing all commands to the user"""
    def get_command_list(self):
        command = f'\n Enter [Shortcut Keys or Command] '
        for k, v in self.list_of_commands.items():
            command += f'\n[{k} or {v[0]}] : {v[1]}'
        return command

    def what_command(self, the_command):
        # Input from users are designed not to be case sensitive
        command = the_command.upper()
        if command == 'P' or command == 'PENSIZE':
            self.drawer.select_pen(self.data)
        elif command == 'D' or command == 'PENDOWN':
            self.drawer.pen_down()
            self.is_pen_down = True
        elif command == 'U' or command == 'PENUP':
            self.drawer.pen_up()
            self.is_pen_down = False
        else:
            # looking through the configurable lookup table
            for k, v in self.list_of_commands.items():
                if command == k or command == v[0]:
                    if not self.is_pen_down:
                        return
                    else:
                        self.drawer.draw_line(int(v[2]), self.data)
                        return
            # Error handling if command is not in the lookup table
            if command not in self.list_of_commands.keys():
                self.message = (f'{command} command is not found!\nChoose from the command below \n'
                                f'{self.get_command_list()}')
                print(f'{self.message}')


class MySourceReader:

    # This is where view and parser interact
    def __init__(self, the_view, the_parser):
        super().__init__()
        self.view = the_view
        self.parser = the_parser
        self.source = []

    def go(self):
        self.view.show_greetings()
        commands = self.view.input_command().split(',')
        for command in commands:
            self.source.append(command)
        self.parser.parse(self.source)


if __name__ == "__main__":
    #  Here it is flexible because it will take any Subclass of views, Parser, and drawer
    # Extending the SourceReader and making it more flexible
    # Comment out the views that wants to be used
    # view = TheView()
    # view = TkinterView()

    # mainloop()
    import doctest
    doctest.testmod(verbose=True)
