__author__ = 'attakei'

import unittest
from ticktask.resources import HtmlResource, ContentType


class HtmlResourceTest(unittest.TestCase):
    def setUp(self):
        self.resource = HtmlResource()

    def test_it(self):
        self.assertEqual(self.resource._assets, [])
        self.assertEqual(self.resource.assets, [])

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

    def test_add_js_expressly(self):
        self.resource.add_js('http://example.com/static/main.js')
        asset_type, asset_url = self.resource.assets[0]
        self.assertEqual(asset_type, ContentType.js)
        self.assertEqual(asset_url, 'http://example.com/static/main.js')

    def test_add_css_expressly(self):
        self.resource.add_css('http://example.com/static/main.css')
        asset_type, asset_url = self.resource.assets[0]
        self.assertEqual(asset_type, ContentType.css)
        self.assertEqual(asset_url, 'http://example.com/static/main.css')


if __name__ == '__main__':
    unittest.main()
