# -*- coding:utf8 -*-
__author__ = 'attakei'
__doc__ = """TickTask web server context resource module.
"""

from pyramid.decorator import reify


class HtmlResource(object):
    """HTMLレスポンスを返すcontextにおけるリソース

    """
    __name__ = None

    def __init__(self, title=None):
        self._title = title
        self._subtitle = None

    @reify
    def title(self):
        """HTMLタイトル"""
        if self._subtitle is None:
            return self._title
        if self._title is None:
            return self._subtitle
        return '{}: {}'.format(self._title, self._subtitle)

    def set_title(self, title):
        self._subtitle = title
