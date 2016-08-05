from CommonMark import blocks

from Markua.inlines import InlineParser


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
