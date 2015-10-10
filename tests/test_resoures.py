__author__ = 'attakei'

import unittest
from ticktask.resources import HtmlResource


class HtmlResourceTest(unittest.TestCase):
    def setUp(self):
        self.resource = HtmlResource()

    def test_init__with_args(self):
        resource = HtmlResource('Main Title')
        self.assertEqual(resource._title, 'Main Title')

    def test_title__none_title(self):
        self.assertEqual(self.resource.title, None)

    def test_title__with_title(self):
        self.resource._title = 'Main Title'
        self.assertEqual(self.resource.title, 'Main Title')

    def test_set_title__none_base_title(self):
        self.resource.set_title('sub title')
        self.assertEqual(self.resource.title, 'sub title')

    def test_set_title__with_title(self):
        resource = HtmlResource('Main')
        resource.set_title('sub title')
        self.assertEqual(resource.title, 'Main: sub title')


if __name__ == '__main__':
    unittest.main()
