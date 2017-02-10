## empowered by (Liftoff)[https://github.com/LiftoffSoftware/htmltag.git]
##

import re
import sys
from types import ModuleType

self_closing_tags = set([
    'area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img', 'input',
    'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr',
])

whitelist = set([
    'a', 'abbr', 'aside', 'audio', 'bdi', 'bdo', 'blockquote', 'canvas',
    'caption', 'code', 'col', 'colgroup', 'data', 'dd', 'del',
    'details', 'div', 'dl', 'dt', 'em', 'figcaption', 'figure', 'h1',
    'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'img', 'ins', 'kbd', 'li',
    'mark', 'ol', 'p', 'pre', 'q', 'rp', 'rt', 'ruby', 's', 'samp',
    'small', 'source', 'span', 'strong', 'sub', 'summary', 'sup',
    'table', 'td', 'th', 'time', 'tr', 'track', 'u', 'ul', 'var',
    'video', 'wbr'
])

re_html_tag = re.compile("(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>")

basic_html_frame = '''
<!DOCTYPE html><html><head></head><body>%s</body></html>
'''

class HTML(unicode):
    tagname = None

    def append(self, *string):
        close_tag_start = self.rfind('</')
        if self.tagname:
            close_tag_start = self.rfind('</'+self.tagname)

        if close_tag_start == -1:
            return self + "".join(string)
        ending = self[close_tag_start:]
        beginning = self[:close_tag_start]
        if self.tagname:
            tagname = self.tagname
            new = HTML(beginning + "".join(string) + ending)
            new.tagname = tagname
            return new
        else:
            return HTML(beginning + "".join(string) + ending)


class Tag(object):
    """
    function to wrap string in any given html tag
    The `Tag` class must be used in a direct fashion:
    >>> from htmlwriter import Tag
    >>> b = Tag('b')
    >>> print(b('strong'))
    <b>strong</b>

    The `Tag` class must recognise self closing tag and treat it differently:
    >>> from htmlwriter import Tag
    >>> img = Tag('img')
    >>> print(img(href="http://www.google.com"))
    <img href="http://www.google.com">
    """

    def __init__(self, tagname, **kwargs):
        self.tagname = tagname

    def __call__(self, *args, **kwargs):
        return self.wrap(self.tagname, *args, **kwargs)

    @staticmethod
    def wrap(tag, *args, **kwargs):
        template = "<{tagstart}>{content}</{tag}>"
        if tag in self_closing_tags:
            template = "<{tagstart}>"
        content=""
        for string in args:
            content += string
        tagstart = tag
        if kwargs:
            tagstart += " "
            for key, value in kwargs.items():
                if value == True:
                    tagstart = tagstart + key + " "
                elif value == False:
                    continue
                else:
                    tagstart = tagstart + '{key}="{value}" '.format(key=key, value= value)

            tagstart = tagstart.rstrip()
        html = template.format(tagstart=tagstart, content=content, tag=tag)
        html = HTML(html)
        html.tagname = tag
        return html


class SelfWrap(ModuleType):
    def __init__(self, tagname, *args, **kwargs):
        no_override = [
            'HTML', 'SelfWrap', 'Tag', 'strip_xss', '__author__',
            '__builtins__', '__doc__', '__license__', '__name__',
            '__package__', '__version__', '__version_info__'
        ]

        for attr in no_override:
            setattr(self, attr, getattr(tagname, attr, None))

    def __getattr__(self, name):
        if name not in self.__dict__:
            setattr(self, name, Tag(name))
        return self.__dict__[name]

    def __call__(self, *args, **kwargs):
        return Tag(self.tagname, *args, **kwargs)

if __name__ == "__main__":
    """
    Execute python `htmlwriter.py -v` to run the testing case
    """
    import doctest
    doctest.testmod()

else:
    self = sys.modules[__name__]
    sys.modules[__name__] = SelfWrap(self)