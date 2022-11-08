from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.livecoinwatch.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

data_rows = soup.findAll("tr", attrs={"class": "table-row filter-row"})

idx_counter = 1
output_counter = 1

for row in data_rows:
    data_cells = row.findAll("td")
    symbol = data_cells[idx_counter].text.split()[0]
    name = data_cells[idx_counter].text.split()[1]
    current_price = data_cells[idx_counter + 1].text
    change_over_24_hrs = data_cells[idx_counter + 7].text

    current_price_for_calc = float(current_price.replace('$',''))

    if symbol == 'BTC' and current_price_for_calc < 40000:
        print('e')

    if symbol == 'ETH' and current_price_for_calc < 3000:
        print('e')

    
    adjusted_24_hr_percent = float(str('.0') + change_over_24_hrs.strip('%').replace('.',''))
    adjusted_price_based_on_percent = adjusted_24_hr_percent * float(current_price.replace('$',''))

    
    if output_counter <= 5:
        print(f'Symbol: {symbol}')
        print(f'Cryptocurrency Name: {name}')
        print(f'Current price: {current_price}')
        print(f'% Change (past 24 hrs): {change_over_24_hrs}')
        print(f'Price accounting for 24-hr % change: ${adjusted_price_based_on_percent}')
        print()
    
    output_counter += 1
