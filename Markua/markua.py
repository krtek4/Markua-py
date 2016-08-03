#!/usr/bin/env python
from __future__ import unicode_literals
import argparse
import sys
import Markua


def main():
    parser = argparse.ArgumentParser(
        description="Process Markua according to specification.")
    parser.add_argument(
        'infile',
        nargs="?",
        type=argparse.FileType('r'),
        default=sys.stdin,
        help="Input Markua file to parse, defaults to STDIN")
    parser.add_argument(
        '-o',
        nargs="?",
        type=argparse.FileType('w'),
        default=sys.stdout,
        help="Output HTML/JSON file, defaults to STDOUT")
    parser.add_argument('-a', action="store_true", help="Print formatted AST")
    parser.add_argument('-aj', action="store_true", help="Output JSON AST")
    args = parser.parse_args()
    parser = Markua.Parser()
    f = args.infile
    o = args.o
    lines = []
    for line in f:
        lines.append(line)
    data = "".join(lines)
    ast = parser.parse(data)
    if not args.a and not args.aj:
        renderer = Markua.HtmlRenderer()
        o.write(renderer.render(ast))
        exit()
    if args.a:
        # print ast
        Markua.dumpAST(ast)
        exit()

    # o.write(ast.to_JSON())
    o.write(Markua.dumpJSON(ast))
    exit()


if __name__ == '__main__':
    main()
