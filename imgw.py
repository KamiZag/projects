from requests import get
from json import loads
from terminaltables import AsciiTable

CITIES = ['Gdańsk', 'Warszawa']

def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    
    rows = [
        ['Miasto', 'data_pomiaru','Godzina pomiaru', 'Temperatura', 'Ciśnienie']
    ]

    for row in loads(response.text):
        
        if row['stacja'] in CITIES:
            rows.append([
                row['stacja'],
                row['data_pomiaru'],
                row['godzina_pomiaru'],
                row['temperatura'],
                row['cisnienie']
            ])
    table = AsciiTable(rows)
    print(table.table)        
           
if __name__ == '__main__':
    print('pogodynka 2022')
    main() 
    
