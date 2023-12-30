from spellchecker import SpellChecker
from gingerit.gingerit import GingerIt
ch=GingerIt()

ta="i loev yuo"


print(ch.parse(ta))
t=ch.parse(ta)
h=t['corrections']

    
def correct(item):
    #t=ch.parse(item)
    #h=t['corrections']
    last=0
    st=0
    for i in item:
        st=i['start']
        last=st+len(i['text'])
        print(st)
        print(last)
    
        
correct(h)    
