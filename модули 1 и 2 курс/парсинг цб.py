url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
# date = 'date_req=26/01/2023'
# today = datetime.today()
today = today.strftime('%d/%m/%Y')
date = {'date_req' : today}

responce = requests.get(url, params = date)

xml = BeautifulSoup(responce.content, 'html.parser')

def getCourse(id):
    course = xml.find("valute", {'id':id}).value.text
    return course

print(getCourse("R01280"), 'рублей за 10000 инденезийских рупий')
print(getCourse("R01235"), 'рублей за 1 доллар')
print(getCourse("R01239"), 'рублей за 1 евро')