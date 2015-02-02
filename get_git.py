import re
import ConfigParser
import urllib 
import git, os, shutil
from HTMLParser import HTMLParser
from git import Repo
from subprocess import call, STDOUT
import os
var1 = raw_input("Enter Config File: ")
myfile= open(var1, 'r')
for line in myfile:
     line = line.rstrip()
     url_match= re.search("(?P<url>https?://[^\s]+)", line)
     if url_match is not None: 
         print url_match.group("url")
         var2 = str(url_match.group("url"))

class parseclass(HTMLParser):
        def handle_data(self, data):
            print "Encountered some data  :", data


parser = parseclass()
parser.feed(var2)

                                      
sock = urllib.urlopen(var2) 
parsepage = sock.read()                            
                                     
junk = parsepage
pat = re.compile(r'https://github.com[^\s<>"]*')
#pat.findall(junk) 
if pat is not None: 
 var3 = str(pat.findall(junk))
else:
 print "NOMATCH"
var4= str(var3)[1:-1]
#var4 = re.sub('[!@#$]', '', var4)
#line = var4.translate(None, ',')
nline = var4.replace("'","")
arr = nline.split(",")
#Checking the links on page 
#cloning the valid one and catching the exception for invalid links 
for word in arr:

 nwrd= word +".git"
 print (nwrd)

 class parsegit(HTMLParser):
        def handle_data(self, data):
              self.output.append(data)
              print "Encountered git url to clone:",data
        def feed(self, data):
              self.output = []
              HTMLParser.feed(self, data)
		
 parser = parsegit()        
 parser.feed(nwrd)

 wrd = parser.output
 nwrd= str(wrd)[2:-2]
 newrd=nwrd.strip()

 config = ConfigParser.ConfigParser()
 config.read(var1)
 root_directory = config.get('mygit', 'root_directory')
 
 try:
  #cloning the valid links
  repo_path = root_directory
  new_repo = Repo.clone_from(newrd, repo_path)
  print "Clone Complete"
 except: # catch exceptions for the invalid links
  e = sys.exc_info()[0]



 
