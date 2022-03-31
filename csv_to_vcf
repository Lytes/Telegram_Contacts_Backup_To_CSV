# Can't keep having to write this everytime
# Just full name and telephone, can be edited
import csv

input=list(csv.reader(open('newcont.csv','r')))
output=open('charity.vcf','w')
for row in input:
        output.write("BEGIN:VCARD\n")
        output.write("VERSION:4.0\n")
        output.write("FN:"+row[0]+"\n")
        output.write("TEL;TYPE=HOME,VOICE:"+row[1]+"\n")
        output.write("END:VCARD\n")
output.close()
