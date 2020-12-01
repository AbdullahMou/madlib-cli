from madlib_cli import __version__
from madlib_cli.madlib import *


def test_version():
    assert __version__ == '0.1.0'

def test_temp():
    act=read_template()
    exp=''
   assert act==exp 

   def test_parse():
    act=parse(read_template())
    exp=''
   assert act==exp 

    def test_merge():
    act=merge(parse(),anser)
    exp=''
   assert act==exp 