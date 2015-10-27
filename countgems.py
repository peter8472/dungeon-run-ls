import os
import dr
from xml.dom import minidom
# we'll open first and forth, which should be the most different
def get_thorpin_sapphire_count():
    pass

if __name__ == "__main__":
    mydata = dr.getfile("first")
    thexml = mydata.xml
    mychar = mydata.getChar("thorpIn")
    mygame = mychar.getElementsByTagName("game")[2]
    mygems = mygame.getElementsByTagName("gemstones")[1]
    myitems = mygems.getElementsByTagName("item")
    for x,y in enumerate(myitems):
        print x,y
