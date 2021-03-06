#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  f=open(filename,'r')
  text=f.read()
  #print(text)
  namelist=[]
  year_match=re.search(r'Popularity\sin\s(\d\d\d\d)',text)
  if not year_match:
    # We didn't find a year, so we'll exit with an error message.
    sys.stderr.write('Couldn\'t find the year!\n')
    sys.exit(1)
  
  #print(m.group(1))
  namelist.append( year_match.group(1))
  names=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',text)
  d={}
  for rank,boyname,girlname in names:
    #print('{0} {1}  {2}'.format(rank,boyname,girlname))
    if boyname not in d:
      d[boyname]=rank
    if girlname not in d:
      d[girlname]=rank

  for k in sorted(d.keys()):
    namelist.append(k + ' '+d[k])
  #print(names)
  f.close()
  return namelist
'''
 for n in names:
    if n[1] not in d:
      d[n[1]]=n[0]
    elif  n[2] not in d:
        d[n[2]]=n[0]
  
  for k in sorted(d.keys()):
    print('{0} -> {1}'. format(k,d[k]))
'''
#
  


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)
  #extract_names(args[0])
  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
    names = extract_names(filename)
   # print(names)
    # Make text out of the whole list
    text = '\n'.join(names)
  print (text)
  
if __name__ == '__main__':
  main()
