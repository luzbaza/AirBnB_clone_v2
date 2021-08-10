#!/usr/bin/python3
""" """

import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

class TConsole(unittest.TestCase):
    """ """
    def testDoCreate(self):
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("create City name=\"California\"")
        city_id = out.getvalue()
        self.assertTrue(len(city_id) >= 1)

        with patch('sys.stdout', new=StringIO()) as out2:
            HBNBCommand().onecmd("show City " + city_id)
        str = out2.getvalue()
        p = "'name': 'California'"
        self.assertTrue(p in str)
