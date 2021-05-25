# Наименование вакансии.
# Предлагаемую зарплату (отдельно минимальную и максимальную).
# Ссылку на саму вакансию.
# Сайт, откуда собрана вакансия. ### По желанию можно добавить ещё параметры вакансии
# (например, работодателя и расположение). Структура должна быть одинаковая для вакансий с
# обоих сайтов. Общий результат можно вывести с помощью dataFrame через pandas.
import time
from bs4 import BeautifulSoup as bs
import requests
import pprint
import lxml
import numpy as np
url = 'https://hh.ru'
params = {'clusters': 'true','area':'1','experience':'noexperience','enable_snippets':'false','salary':'','st':'searchVacancy','text': input("Please, enter the required vacancy: "), 'from':'suggest_post','page': 0}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}


params['page'] = int(params['page'])
vacancies = []
list = list(range(3))
for number in list:
    params['page'] = list[0]
    list.pop(0)
    if list[0] == 2:
        break


    response = requests.get(url + '/search/vacancy', params=params, headers=headers)
    dom = bs(response.text, 'lxml')

    vacancy_list = dom.find_all('div',{'class':'vacancy-serp-item'})

    for vacancy in vacancy_list:
        current_vacancy = {}
        vacancy_data = vacancy.find('a',{'class':'bloko-link'})
        vacancy_link = vacancy_data['href']
        vacancy_name = vacancy_data.text
        vacancy_compensation_div = vacancy.find('div',{'class':'vacancy-serp-item__sidebar'})
        vacancy_compensation = vacancy_compensation_div.find('span',{'data-qa':'vacancy-serp__vacancy-compensation'})
        if vacancy_compensation == None:
            vacancy_compensation = "Salary not specified"
        else:
            vacancy_compensation = vacancy_compensation.text

        current_vacancy['name'] = vacancy_name
        current_vacancy['link'] = vacancy_link
        current_vacancy['compensation'] = vacancy_compensation
        vacancies.append(current_vacancy)
        time.sleep(2)

print(vacancies)
print(len(vacancies))