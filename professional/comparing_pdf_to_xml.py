import os
import PyPDF2
import pandas as pd
from thefuzz import fuzz
import xml.etree.ElementTree as ET

pdf_dir = r'path/to/pdf/directory'
xml_dir = r'path/to/xml/directory'

pdf_file = pdf_dir + '\\' + r'Invoice_120459_PO5000232985_20230524.pdf'
xml_file = xml_dir + '\\' + r'Invoice_120459_PO5000232985_20230524.xml'

# reading pdf
read = PyPDF2.PdfReader(pdf_file)
# getting text from first page
pdf_txt = read.pages[0].extract_text()

# reading xml
with open(xml_file) as xml:
    xml_tree = ET.fromstring(xml.read())

cols = ['pdf_value','xml_value','xml_tag','fuzz_ratio']
df_matches = pd.DataFrame(columns=cols)
for x in pdf_txt.split('\n')[7:]:
    chk = False
    for y in xml_tree.iter():
        if fuzz.ratio(x,y.text) > 52:
            df_matches.loc[len(df_matches)] = [x,y.text,y.tag,fuzz.ratio(x,y.text)]
            chk = True
            break
    if chk == False:
        df_matches.loc[len(df_matches)] = [x,'no match',None,None]
display(df_matches)