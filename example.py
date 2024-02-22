from cne_scrapper import get_name

n = input('Nacionalidad: ')
ci = input('CI: ')

result = get_name(n, ci)

if result:
    print('Nombre:', result)
else:
    print('No encontrado')