from bs4 import BeautifulSoup
import urllib.request
import ssl
import csv

ssl._create_default_https_context = ssl._create_unverified_context

with open('venezolanos.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Cedula', 'Nombre'])
	
	for i in range(40000000):
		try:
			web = urllib.request.urlopen(f'http://www.cne.gob.ve/web/registro_electoral/ce.php?nacionalidad=V&cedula={i}').read().decode()
			parsed_html = BeautifulSoup(web, 'html.parser')
			td = parsed_html.find_all('td', attrs={'align':'left'})
			writer.writerow([td[1].getText(), td[3].getText()])
		except Exception as e:
			pass

print('Done!')