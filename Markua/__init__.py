# flake8: noqa
from __future__ import unicode_literals, absolute_import

from Markua.blocks import Parser
from Markua.dump import dumpAST, dumpJSON
from Markua.renderer.html import HtmlRenderer


def markua(text, format="html"):
    parser = Parser()
    ast = parser.parse(text)
    if format not in ["html", "json", "ast"]:
        raise ValueError("format must be 'html', 'json' or 'ast'")
    if format == "html":
        renderer = HtmlRenderer()
        return renderer.render(ast)
    if format == "json":
        return dumpJSON(ast)
    if format == "ast":
        return dumpAST(ast)
