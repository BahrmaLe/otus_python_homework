"""Parser"""
from html.parser import HTMLParser


class GetHTMLContent(HTMLParser):
    """Class for getting HTML Code and parsing it"""
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.img = []
        self.tags = []
        self.full_tags = []

    def handle_starttag(self, tag, attrs):
        # for name, value in attrs:
        self.full_tags.append(tag + str(attrs))
        self.tags.append(tag)

        if tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    self.links.append(value)
        if tag == 'img':
            for name, value in attrs:
                if name == 'src':
                    self.img.append(value)


