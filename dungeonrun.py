#! /usr/bin/python
"""Xmlgame: does xmlstuff
jsgame:  does js stuff
App: gets clipboard and runs UI

Right now everythign depends on the UI being up and running.  This won't always be the case, and isn't necessary.
"""
import Tkinter 
import os
import re
from Tkconstants import *
import sys
import json
from xml.dom import minidom
def cb():
    u = Tkinter.Tk()
    v =u.clipboard_get()
    u.destroy()
    return v


class badXmlgame():
    """ I want to make this inherit from minidom
It's not working  yet"""
    chars = { "2":"Thorpin", "1":"Featherwell", "3":"Ganelon", 	"4":"Pippen"}

    def __init__(self,parsed_json):
	tmp = parsed_json['json']
	tmp = tmp['response']
	tmp = tmp['properties']
	tmp = tmp['value']
	self.xml = minidom.parseString(tmp)

    def show_size(self):    
	games = self.xml.getElementsByTagName("game")
    	for i in games:
            charName = self.chars[i.parentNode.getAttribute("charId")] 
            length = len(i.toxml())
            print "%s %d" % (charName, length)
    def toxml(self):
	return self.xml.toxml()


class Xmlgame():
    """holds the interpreted xml from the json"""
    chars = { "2":"Thorpin", "1":"Featherwell", "3":"Ganelon", 	"4":"Pippen"}

    def __init__(self,parsed_json):
	tmp = parsed_json['json']
	tmp = tmp['response']
	tmp = tmp['properties']
	tmp = tmp['value']
	self.xml = minidom.parseString(tmp)

    def getChar(self,name):
	"""get a character given the character name.
Not case sensistive"""
	mychars = self.xml.getElementsByTagName("data")
	for i in mychars:
	    charnum = i.getAttribute("charId")
	    charname = Xmlgame.chars[charnum]

	    if re.match("(?i)%s" %(charname), name):
		return i
	raise NameError, "%s is not a valid name" % (name)

    def show_size(self):    
	games = self.xml.getElementsByTagName("game")
    	for i in games:
            charName = self.chars[i.parentNode.getAttribute("charId")] 
            length = len(i.toxml())
            print "%s %d" % (charName, length)
    def toxml(self):
	return self.xml.toxml()


class App:
  def __init__(self, master):
    self.master = master # This is not legitimate use of "master"
    cbstats = "Get Stats from the clipboard"
    frame = Tkinter.Frame(master, relief = RIDGE, borderwidth=2)
    frame.pack(fill = BOTH, expand=1)
    label = Tkinter.Label(frame, text="hello world")
    label.pack(fill=X, expand=1)
    button = Tkinter.Button( frame, text="exit", command=u.destroy)
    button2 = Tkinter.Button( frame, text="hello", command=self.say_hi)
    button.pack(side=BOTTOM)
    button2.pack(side=BOTTOM)
    button3 = Tkinter.Button( frame, text=cbstats, command=self.blah)
    button3.pack(side=RIGHT)
  def blah(self):
      tmp = self.master.clipboard_get()	
      print "size is %d" % (len(tmp))

      g = json.loads(tmp)
      game = Xmlgame(g)
      game.show_size()
#      print game.toxml()

  def say_hi(self):
	print "hi there"

def savecb(filename):
    stuff = cb()
    if os.path.exists(filename):
	raise NameError, "file exists"
    with open(filename,'w') as f:
	f.write(stuff)
    
def getcb():
    stuff = cb()
    js = json.loads(stuff)
    return Xmlgame(js)
def getfile(fname):
    with open(fname) as infile:
	js = json.load(infile)
    return Xmlgame(js)


    
if __name__ == "__main__":
    if len(sys.argv) != 2:
	print "usage: %s <filename>"
        u = Tkinter.Tk()
	app  = App(u)
	u.mainloop()
	exit(1)
    with open(sys.argv[1]) as f:
        tmp = f.read()
        parsed_json = json.loads(tmp)
    print "Total length %d" % ( len(tmp))
    blah = Xmlgame(parsed_json)
    blah.show_size()
