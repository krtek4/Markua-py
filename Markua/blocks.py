from CommonMark import blocks

from Markua.inlines import InlineParser


class BlurbBlock(blocks.Block):
    @staticmethod
    def blurb_continue(start_char, parser=None, container=None):
        ln = parser.current_line

        if not parser.indented and \
               blocks.peek(ln, parser.next_nonspace) == start_char and \
               blocks.peek(ln, parser.next_nonspace + 1) == '>':
            parser.advance_next_nonspace()
            parser.advance_offset(2, False)
            if blocks.is_space_or_tab(blocks.peek(ln, parser.offset)):
                parser.advance_offset(1, True)
        else:
            return 1
        return 0

    @staticmethod
    def continue_(parser=None, container=None):
        BlurbBlock.blurb_continue('B', parser, container)

    @staticmethod
    def finalize(parser=None, block=None):
        return

    @staticmethod
    def can_contain(t):
        return True


class AsideBlock(BlurbBlock):
    @staticmethod
    def continue_(parser=None, container=None):
        BlurbBlock.blurb_continue('A', parser, container)


class BlockStarts(blocks.BlockStarts):
    # We create a new methods array for the following reasons :
    # * Markua disallows HTML blocks
    METHODS = [
        'block_quote',
        'atx_heading',
        'fenced_code_block',
        'setext_heading',
        'thematic_break',
        'list_item',
        'indented_code_block',
    ]


class Parser(blocks.Parser):
    def __init__(self, options={}):
        super(Parser, self).__init__(options)

        self.block_starts = BlockStarts()
        self.inline_parser = InlineParser(options)
