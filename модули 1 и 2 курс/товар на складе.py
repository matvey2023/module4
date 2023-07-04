goods={
    'Лампа' : '12345',
    'Стол' : '23456',
    'Диван' : '34567',
    'Стул' : '45678'
}
store={
    '12345' : [
        {'quantitly':27, 'price':42},
    ],
    '23456' : [
        {'quantitly':22, 'price':510},
        {'quantitly':32, 'price':520}
    ],
    '34567': [
        {'quantitly': 2, 'price': 1200},
        {'quantitly': 1, 'price': 1150}
    ],
    '45678': [
        {'quantitly': 50, 'price': 100},
        {'quantitly': 12, 'price': 95},
        {'quantitly': 43, 'price': 97}
    ],
}
for tovar in goods:
    summa = 0
    kol_vo=0
    for z in store[goods[tovar]]:
        summa += z['quantitly'] * z['price']
        kol_vo += z['quantitly']
    print(tovar," - ", kol_vo, "штук, стоимость:", summa)