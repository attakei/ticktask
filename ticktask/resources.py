# -*- coding:utf8 -*-
__author__ = 'attakei'
__doc__ = """TickTask web server context resource module.
"""

from pyramid.decorator import reify


class ContentType(object):
    js = 'application/javascript'
    css = 'text/css'


class HtmlResource(object):
    """HTMLレスポンスを返すcontextにおけるリソース

    """
    __name__ = None

    def __init__(self, title=None):
        self._title = title
        self._subtitle = None
        self._assets = []

    @reify
    def title(self):
        """HTMLタイトル"""
        if self._subtitle is None:
            return self._title
        if self._title is None:
            return self._subtitle
        return '{}: {}'.format(self._title, self._subtitle)

    @reify
    def assets(self):
        return self._assets

    def set_title(self, title):
        """HTMLページタイトルの追加設定
        """
        self._subtitle = title

    def add_js(self, asset):
        """「このjsを使うよ」という宣言
        """
        self._assets.append((ContentType.js, asset))

    def add_css(self, asset):
        """「このcssを使うよ」という宣言
        """
        self._assets.append((ContentType.css, asset))
