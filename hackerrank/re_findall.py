import re
print "\n".join(re.findall(r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})[^aeiouAEIOU]',raw_input()) or ['-1'])
