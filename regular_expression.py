
import re
phRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
m=phRegex.findall('cell: 415-555-5432 home: 667-715-5555')
print(m)
