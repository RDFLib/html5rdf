
from . import support  # noqa

import html5rdf
from html5rdf.treeadapters import sax
from html5rdf.treewalkers import getTreeWalker


def test_to_sax():
    handler = support.TracingSaxHandler()
    tree = html5rdf.parse("""<html xml:lang="en">
        <title>Directory Listing</title>
        <a href="/"><b/></p>
    """, treebuilder="etree")
    walker = getTreeWalker("etree")
    sax.to_sax(walker(tree), handler)
    expected = [
        'startDocument',
        ('startElementNS', ('http://www.w3.org/1999/xhtml', 'html'),
            'html', {(None, 'xml:lang'): 'en'}),
        ('startElementNS', ('http://www.w3.org/1999/xhtml', 'head'), 'head', {}),
        ('startElementNS', ('http://www.w3.org/1999/xhtml', 'title'), 'title', {}),
        ('characters', 'Directory Listing'),
        ('endElementNS', ('http://www.w3.org/1999/xhtml', 'title'), 'title'),
        ('characters', '\n        '),
        ('endElementNS', ('http://www.w3.org/1999/xhtml', 'head'), 'head'),
        ('startElementNS', ('http://www.w3.org/1999/xhtml', 'body'), 'body', {}),
        ('startElementNS', ('http://www.w3.org/1999/xhtml', 'a'), 'a', {(None, 'href'): '/'}),
        ('startElementNS', ('http://www.w3.org/1999/xhtml', 'b'), 'b', {}),
        ('startElementNS', ('http://www.w3.org/1999/xhtml', 'p'), 'p', {}),
        ('endElementNS', ('http://www.w3.org/1999/xhtml', 'p'), 'p'),
        ('characters', '\n    '),
        ('endElementNS', ('http://www.w3.org/1999/xhtml', 'b'), 'b'),
        ('endElementNS', ('http://www.w3.org/1999/xhtml', 'a'), 'a'),
        ('endElementNS', ('http://www.w3.org/1999/xhtml', 'body'), 'body'),
        ('endElementNS', ('http://www.w3.org/1999/xhtml', 'html'), 'html'),
        'endDocument',
    ]
    assert expected == handler.visited
