# Markua-py

Python implementation of the [Markua specification](http://markua.com/).

The markdown parsing is delegated by [CommonMark-py](https://github.com/rtfd/CommonMark-py).

## Markua specificites compared to Markdown

This is a, hopefully, complete list of differences with Markdown. The checkmark indicates if this part is implemented currently or not.

The order should roughly reflect the order in which items will be implemented.

- [ ] Asides (`A>`)
- [ ] Blurbs (`B>`)
- [ ] Blurbs shortcuts (`D>`, `E>`, `I>`, `Q>`, `T>`, `W>`, `X>`) 
- [ ] Disallow inline HTML
- [ ] Underline with 4 `_` : `____this text is underlined____`
- [ ] Strike-through with 2 `~` : `~~this text is striken through~~`
- [ ] Superscript with `^` : `10 m^2^`
- [ ] Subscript with `~` : `H~2~O`
- [ ] Setext headings does not work (ie `===` and `---`)
- [ ] New "Part heading" : `# This is a part heading #`
- [ ] Except for the part headings, pounds (`#`) at the end of a heading are displayed
- [ ] Numbered lists can be in descending order
- [ ] Numbered list starting "digit" can be specified
- [ ] Definition lists
- [ ] Exactly one new line is a forced line break instead of being ignores
- [ ] New lines after two new lines (new paragraph) are displayed as line breaks
- [ ] Leading whitespace after exactly one new line are displayed
- [ ] `{blockquote}` syntax for blockquotes
- [ ] `{aside}` and `{blurb}` syntax
- [ ] Blurbs "classes" via attributes

The following parts will need more examination before being worked on :

- Tables support
- Ressources / Figures support
- Scene breaks
- Block elements inside paragraphs
- Footnotes and Endnotes
- Metadata / Attributes list
- CriticMarkup

Will probably not be implemented :

- Disallow reference link syntax