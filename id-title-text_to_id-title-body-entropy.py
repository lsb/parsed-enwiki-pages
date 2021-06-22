import mwparserfromhell
import re
import json
import sys
import lzma

def parse_and_strip(mw):
    initial = mwparserfromhell.parse(mw).strip_code()
    stripped = "\n".join([s.strip() for s in initial.splitlines()])
    return re.sub(r'\n\n\n+','\n\n', stripped)

for line in sys.stdin:
  [id,title,text] = json.loads(line)
  parsedtext = parse_and_strip(text)
  entropy = len(lzma.compress(bytes(parsedtext, 'utf-8')))
  sys.stdout.write(json.dumps([id,title,parsedtext,entropy]) + "\n")

