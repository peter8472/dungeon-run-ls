#! /usr/bin/python

from Tkinter import Tk # does not work yet and belongs in another file
import sys
import json
from xml.dom import minidom

def from_cb():
  
  u = Tk()
  tmp = u.clipboard_get()
  g = json.loads(tmp)


chars = { "2":"Thorpin", "1":"Featherwell", "3":"Ganelon", 

"4":"Pippen"}
def getCharMap(parsed):
    pass

def show_size(parsed_json):    
    tmp = parsed_json['json']
    tmp = tmp['response']
    
    tmp = tmp['properties']
    tmp = tmp['value']
    parsed = minidom.parseString(tmp)
#    chars = getCharMap(parsed) someday this might be needed.
    games = parsed.getElementsByTagName("game")
    for i in games:
        charName = chars[i.parentNode.getAttribute("charId")] 
        length = len(i.toxml())
        print "%s %d" % (charName, length)
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
	print "usage: %s <filename>"
	exit(1)
    with open(sys.argv[1]) as f:
        tmp = f.read()
        parsed_json = json.loads(tmp)
    print "Total length %d" % ( len(tmp))
    show_size(parsed_json)
