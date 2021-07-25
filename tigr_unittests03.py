import unittest
from tigrExtend import *
from cli import *


class TestParserAcceptsLongFormCommand(unittest.TestCase):

    def test_parser_draw_line_north_with_a_given_distance(self):
        the_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(the_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append('North 100')
        src_reader.parser.parse(src_reader.parser.source)
        expected_message = 'drawing line of length 100 at 0 direction'
        actual_message = the_drawer.message
        self.assertEqual(expected_message, actual_message)

    def test_parser_draw_line_south_with_a_given_distance(self):
        the_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(the_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append('South 60')
        src_reader.parser.parse(src_reader.parser.source)
        expected_message = 'drawing line of length 60 at 180 direction'
        actual_message = the_drawer.message
        self.assertEqual(expected_message, actual_message)

    def test_parser_draw_line_east_with_a_given_distance(self):
        the_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(the_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append('East 90')
        src_reader.parser.parse(src_reader.parser.source)
        expected_message = 'drawing line of length 90 at 90 direction'
        actual_message = the_drawer.message
        self.assertEqual(expected_message, actual_message)

    def test_parser_draw_line_west_with_a_given_distance(self):
        the_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(the_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append('West 70')
        src_reader.parser.parse(src_reader.parser.source)
        expected_message = 'drawing line of length 70 at 270 direction'
        actual_message = the_drawer.message
        self.assertEqual(expected_message, actual_message)

    def test_parser_draw_line_NORTH_EAST_with_a_given_distance(self):
        the_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(the_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append('North-east 100')
        src_reader.parser.parse(src_reader.parser.source)
        expected_message = 'drawing line of length 100 at 45 direction'
        actual_message = the_drawer.message
        self.assertEqual(expected_message, actual_message)

    def test_parser_draw_line_SOUTH_EAST_with_a_given_distance(self):
        the_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(the_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append('South-east 60')
        src_reader.parser.parse(src_reader.parser.source)
        expected_message = 'drawing line of length 60 at 135 direction'
        actual_message = the_drawer.message
        self.assertEqual(expected_message, actual_message)

    def test_parser_draw_line_SOUTH_WEST_with_a_given_distance(self):
        the_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(the_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append('south-west 90')
        src_reader.parser.parse(src_reader.parser.source)
        expected_message = 'drawing line of length 90 at 225 direction'
        actual_message = the_drawer.message
        self.assertEqual(expected_message, actual_message)

    def test_parser_draw_line_NORTH_WEST_with_a_given_distance(self):
        the_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(the_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append('North-West 70')
        src_reader.parser.parse(src_reader.parser.source)
        expected_message = 'drawing line of length 70 at 315 direction'
        actual_message = the_drawer.message
        self.assertEqual(expected_message, actual_message)


if __name__ == '__main__':
    unittest.main()
