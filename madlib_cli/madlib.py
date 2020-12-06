import re
"""
read the file
"""
def read_template():

  with open('assetes/mad.txt', 'r') as file:
    content=file.read()
    file.close()
    return content


def parse(fun):
    words=[]
    data=re.findall(r"\{.*?\}",fun)
    
    text = re.sub("{[^}]*}", " {}", fun)
    for i in data:
        words.append(i.strip("{ }"))
    return data,text
     

def merge(data,anser):
    sentens = data.format(*anser)
    return sentens



def copyFile(text):
    
    print(text)
    file = open('assetes/mad2.txt','w')
    file.write(text)



if __name__ == "__main__":
  
    content = read_template()
    parts =parse(content)

    anser=[]
    for i in parts[0]:
        msg=input("enter a " +i + " : " )
        anser.append(msg)
    
   
    copy = merge(parts[1],anser)
    copyFile(copy)