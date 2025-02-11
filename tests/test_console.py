#!/usr/bin/python3
""" """

import sys
import unittest
from io import StringIO
from unittest.mock import patch
sys.path.append('/home/klich/AirBnB_clone_v2/')


class TConsole(unittest.TestCase):
    """ """
    def testDoCreate(self):
        from console import HBNBCommand
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("create City name=\"California\"")
        city_id = out.getvalue()
        self.assertTrue(len(city_id) >= 1)

        with patch('sys.stdout', new=StringIO()) as out2:
            HBNBCommand().onecmd("show City " + city_id)
        str = out2.getvalue()
        p = "'name': 'California'"
        self.assertTrue(p in str)
