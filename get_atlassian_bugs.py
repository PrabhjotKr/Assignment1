import re
import StringIO
import os
import ConfigParser
import socket
import urllib2
import random
from time import sleep
var1 = raw_input("Enter bug Config File: ")
myfile= open(var1, 'r')
for line in myfile:
     line = line.rstrip()
     url_match= re.search("(?P<url>https?://[^\s]+)", line)
     if url_match is not None: 
        var2 = str(url_match.group("url"))
config = ConfigParser.ConfigParser()
config.read(var1)
project_tag = config.get('mybug', 'project_tag')
bug_start = config.get('mybug', 'bug_start')
bug_end = config.get('mybug', 'bug_end')
max_timeout_secs = config.get('mybug', 'max_timeout_secs')
root_directory = config.get('mybug', 'root_directory')
dif = int(bug_end) -int( bug_start)
diff =dif+1
bugs = int(bug_start)
buge= int(bug_end)
maxtime = int(max_timeout_secs)
count = 0
while(count<diff):
  url = var2+project_tag+"-"+bug_start
  file_nm= url.split('/')[-1].split('.')[0]
  savepath = root_directory
  comp_Name = os.path.join(savepath, file_nm+".html") 
  response = urllib2.urlopen(url)
  webCnt = response.read()
  f = open(comp_Name, 'w')
  f.write(webCnt)
  f.close 
  count = count+1
  if bugs <= buge:
      bugs = bugs+1
      bug_start = str(bugs)
  b = random.randint(1, maxtime)
  print "random timeout",b
  print "Downloading bug number...",file_nm
  sleep(b)
print "Downloading Complete"



 
