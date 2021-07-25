import unittest
from cli import *


class TestParserAcceptsShortCutCommand(unittest.TestCase):

    def test_parser_draw_line_north_with_a_given_distance(self):
        the_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(the_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append('N 10')
        src_reader.parser.parse(src_reader.parser.source)
        expected_message = 'drawing line of length 10 at 0 direction'
        actual_message = the_drawer.message
        self.assertEqual(expected_message, actual_message)

    def test_parser_draw_line_south_with_a_given_distance(self):
        the_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(the_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append('S 60')
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
        src_reader.parser.source.append('E 90')
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
        src_reader.parser.source.append('W 70')
        src_reader.parser.parse(src_reader.parser.source)
        expected_message = 'drawing line of length 70 at 270 direction'
        actual_message = the_drawer.message
        self.assertEqual(expected_message, actual_message)

    def test_parser_draw_line_NE_with_a_given_distance(self):
        the_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(the_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append('NE 100')
        src_reader.parser.parse(src_reader.parser.source)
        expected_message = 'drawing line of length 100 at 45 direction'
        actual_message = the_drawer.message
        self.assertEqual(expected_message, actual_message)

    def test_parser_draw_line_SE_with_a_given_distance(self):
        the_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(the_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append('SE 60')
        src_reader.parser.parse(src_reader.parser.source)
        expected_message = 'drawing line of length 60 at 135 direction'
        actual_message = the_drawer.message
        self.assertEqual(expected_message, actual_message)

    def test_parser_draw_line_SW_with_a_given_distance(self):
        the_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(the_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append('SW 90')
        src_reader.parser.parse(src_reader.parser.source)
        expected_message = 'drawing line of length 90 at 225 direction'
        actual_message = the_drawer.message
        self.assertEqual(expected_message, actual_message)

    def test_parser_draw_line_NW_with_a_given_distance(self):
        the_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(the_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append('NW 70')
        src_reader.parser.parse(src_reader.parser.source)
        expected_message = 'drawing line of length 70 at 315 direction'
        actual_message = the_drawer.message
        self.assertEqual(expected_message, actual_message)


if __name__ == '__main__':
    unittest.main()
