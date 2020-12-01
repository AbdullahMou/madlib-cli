import re

#read the file

def read_template():

  with open('assetes/mad.txt', 'r') as file:
    content=file.read()
    file.close()
    return print(content)


# read_template()

# ansers from user 
verbing=input('enter a verb-ing : ')
adjective=input('enter a adjective : ')
adverb=input('enter a adverb : ')
anser=[verbing,adjective,adverb]


def parse(fun):
    data=re.findall(r"\{(.*?)\}",fun)
    return data

def merge(string,anser):
    sentens = string.format(*anser)
    return sentens




# data=re.findall(r"\{(.*?)\}",read_template()