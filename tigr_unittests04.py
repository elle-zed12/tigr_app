import unittest
from tigrExtend import *
from cli import *


class TestParserWhenWrongCommandInput(unittest.TestCase):

    def test_parser_draw_when_wrong_command_distance(self):
        the_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(the_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append('N fifty')
        src_reader.parser.parse(src_reader.parser.source)
        expected_message = 'Not a valid value, please enter a valid [direction] [distance]'
        actual_message = src_reader.parser.message
        self.assertEqual(expected_message, actual_message)

    def test_parser_not_to_allow_whitespace_between_direction_distance(self):
        the_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(the_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append('N       80')
        src_reader.parser.parse(src_reader.parser.source)
        expected_message = 'Not a valid value, please enter a valid [direction] [distance]'
        actual_message = src_reader.parser.message
        self.assertEqual(expected_message, actual_message)


if __name__ == '__main__':
    unittest.main()
