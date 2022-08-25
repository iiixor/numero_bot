import requests
import fake_useragent
from bs4 import BeautifulSoup
# import grequests


days = input('Введите день?\n')
months = input('Введите месяц?\n')
years = input('Введите год?\n')

link = f"https://v-kosmose.com/numerologiya/kvadrat-pifagora/?days={days}&month={months}&years={years}"
responce = requests.get(link).text
soup = BeautifulSoup(responce, 'lxml')

block = soup.find('div', class_ = 'pythagoras-square-table')

values = block.find_all('td')

for value in values:

    skill = value.find('b').text
    data = value.text.replace(skill, '')
    print(f'\n{skill} - {data}')

print('')
