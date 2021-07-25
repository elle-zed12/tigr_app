
import json


class MyParser:
    
    def __init__(self, the_drawer):
        super().__init__()
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
        return command.ljust(15) + '\n'

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
                        self.message = 'Pen is up, drawing is disabled'
                        print(f'{self.message}')
                        return
                    else:
                        self.drawer.draw_line(int(v[2]), self.data)
                        return
            # Error handling if command is not in the lookup table
            if command not in self.list_of_commands.keys():
                self.message = (f'{command} command for draw is not found!\nChoose from the command below \n'
                                f'{self.get_command_list()}')
                print(f'{self.message}')


class MySourceReader:
    """ responsible for providing source text for parsing and drawing
        Initiates the Draw use-case.
        Links to a parser and passes the source text onwards """
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

