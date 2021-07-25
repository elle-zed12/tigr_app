import unittest
from cli import *


class TestParser(unittest.TestCase):

    def test_parser_sets_pensize(self):
        a_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(a_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append("Pensize 50")
        src_reader.parser.parse(src_reader.parser.source)
        self.assertTrue(src_reader.parser.data == 50)

    def test_parser_if_penup_is_pendown_equals_false(self):
        the_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(the_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append('penup')
        src_reader.parser.parse(src_reader.parser.source)
        self.assertFalse(the_drawer.is_pen_down)

    def test_parser_if_pendown_equals_true(self):
        the_drawer = TurtleDrawer()
        a_parser = tIgr.MyParser(the_drawer)
        src_reader = tIgr.MySourceReader(TheView, a_parser)
        a_cli = CommandLine(src_reader)
        src_reader.view = a_cli
        src_reader.parser.source.append('pendown')
        src_reader.parser.parse(src_reader.parser.source)
        self.assertTrue(the_drawer.is_pen_down)


if __name__ == '__main__':
    unittest.main()
