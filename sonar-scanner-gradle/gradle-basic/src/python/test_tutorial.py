from tutorial import say_hello
from unittest import TestCase
from io import StringIO
from unittest.mock import patch


class PrintingTest(TestCase):

    def test_say_hello(self):
        name = 'test'
        expected_output = 'Hello {}\n'.format(name)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            say_hello(name)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_say_hello_noname(self):
#         name = ''
        name = 'Stranger'
        expected_output = 'Hello Stranger\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            say_hello(name)
            self.assertEqual(fake_out.getvalue(), expected_output)
