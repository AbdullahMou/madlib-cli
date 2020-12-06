from madlib_cli import __version__
from madlib_cli.madlib import *


def test_version():
    assert __version__ == '0.1.0'

def test_temp():
    act = read_template()
    exp = 'I thought{verb-ing} was a very{adjective} idea. In swimming class, we needed to swim extremely{adverb}, or else we would have to swim longer.'
    assert act == exp

def test_parse():
    act = parse('I thought {verb-ing} was a very {adjective} idea.')
    exp = (['{verb-ing}', '{adjective}'], "I thought  {} was a very  {} idea.")
    assert act == exp

def test_merge():
    act = merge("I thought {} was a very {} idea.",['verb-ing', 'adjective'])
    exp = 'I thought verb-ing was a very adjective idea.'
    assert act == exp