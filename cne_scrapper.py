from bs4 import BeautifulSoup
import urllib.request


def get_name(nacionalidad: str, ci: str) -> str:
	try:
		web = urllib.request.urlopen(f'http://www.cne.gob.ve/web/registro_electoral/ce.php?nacionalidad={nacionalidad.upper()}&cedula={ci}').read().decode()
		parsed_html = BeautifulSoup(web, 'html.parser')
		td = parsed_html.find_all('td', attrs={'align':'left'})
		return (td[3].getText())
	except Exception as e:
		return None
