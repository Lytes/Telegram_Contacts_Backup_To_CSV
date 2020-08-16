pathToFile = './contacts.html' 

with open(pathToFile, encoding='utf-8') as f:

	lines = tuple(l for l in f.readlines())

	with open('ConvertedToCSV.csv', "w", encoding="utf-8") as outputFile:
		#outputFile.write('Name, Number\n')

		for i,l in enumerate(lines):

			if '<div class="name bold">' in l and '<div class="details_entry details">' in lines[i+4]:	
				tel = lines[i+5].replace(' ','')

				if tel.startswith('00234'):
					outputFile.write(lines[i+1].replace('\n','').replace(',','').replace(",","").replace('&apos;','') + ', ' + tel.replace('00234', '0'))		
				else:
					outputFile.write(lines[i+1].replace('\n','').replace(',','').replace(",","").replace('&apos;','') + ', ' + tel)
