import re
import requests
import os


bibliography = ''
for filename in os.listdir('.'):
    if filename.endswith(".tex"):
        print('Scanning file', filename, 'for ADS references')
        texfile = open(filename, 'r')
        filetext = texfile.read()
        texfile.close()
        matches = re.findall("{[0-9]{4}[a-zA-Z0-9., ]*}", filetext)
        splitlist = [i.split(',', 1)[0] for i in matches]
        remove_brackets = [s.strip('}') for s in splitlist]
        remove_brackets2 = [s.strip('{') for s in remove_brackets]
        no_duplicate_list = list(set(remove_brackets2))
        print('Found', len(no_duplicate_list), 'unique ADS references (total', len(matches),')')
        for current_match in range(len(no_duplicate_list)):
            # Fetch bibtex entry from ADS
            bibcode = no_duplicate_list[current_match]
            url = 'http://adsabs.harvard.edu/cgi-bin/nph-bib_query?bibcode=' + bibcode + '&data_type=BIBTEX&db_key=AST&nocookieset=1'
            bibtex_string = requests.get(url)
            # Check if we got a valid bibtex entry
            if bibtex_string.text[113:114] == '@':
                bibliography = bibliography + bibtex_string.text[113:-1]
                print(bibcode, 'successfully retrieved')
            else:
                print(bibcode, 'failed')

print('Writing results to file bibliography.bib...')
with open("bibliography.bib", 'w') as myfile:
    myfile.write(bibliography)
print('Done, see you next time!')
