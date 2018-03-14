#DB Management Mini Project 5
#Question 1
import csv

#Open CSV data
baseballcsv = "/home/gsturrock/Downloads/baseball_salaries_2003-1.csv"
csvData = csv.reader(open(baseballcsv, 'r'),delimiter=',')

#Begin writing XML file
xmlData = open('baseball.xml', 'w')
xmlData.write('<?xml version="1.0"?>' + '\n')
xmlData.write('<baseballsalaries>' + "\n")

#Skip header row
next(csvData, None)

#Write CSV data to XML structure
for row in csvData:
    xmlData.write('  ' + '<player>' + '\n')
    xmlData.write('    ' + '<team>' + row[0] + '</team>' + '\n')
    xmlData.write('    ' + '<name>' + row[1] + '</name>' + '\n')
    xmlData.write('    ' + '<salary>' + row[2] + '</salary>' + '\n')
    xmlData.write('    ' + '<position>' + row[3] + '</position>' + '\n')
    xmlData.write('  ' + '</player>' + '\n')

xmlData.write('</baseballsalaries>')
xmlData.close()

#Question 2
#Write XML data to Pandas dataframe
import xml.etree.ElementTree as ET
import pandas as pd

xmlData2 = open('baseball.xml').read()

root = ET.XML(xmlData2)
baseballdf = []
for i, child in enumerate(root):
    record = {}
    for subchild in child:
        record[subchild.tag] = subchild.text
    baseballdf.append(record)

baseballdf = pd.DataFrame(baseballdf)
baseballdf['salary'] = baseballdf['salary'].apply(pd.to_numeric)

#Do average by position calculations against baseballdf dataframe
avgsal = baseballdf.groupby(['position'])
avgsal = avgsal.mean()
avgsal = avgsal.sort_values('salary', ascending=[False])

#Write avgsal to file
avgsal.to_csv('avgsal.csv', encoding='utf-8')