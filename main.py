import pandas as pd
import csv

# while True:
#     data = pd.read_csv('04UG.csv', encoding='utf-8')
#     print(type(data))
# # print(data.info())
#     d = data['tripduration']
# # print(d)
#     try:
#         h = int(input())
#         for en, var in enumerate(d):
#     # print (type(var))
#             if var == h:
#         # print(en+1)
#                 f = data.iloc[[en+1]]
#                 print(f)
#         if h == 'q':
#             break
#     except:
#         print('ValueError: invalid literal for int() with base 10')

data = pd.read_excel('abc.xlsx')
# print(data.info())
d = data['ID СКУП']
while True:
    print("Введите ID СКУП:")
    try:
        inp = int(input())
        for en, var in enumerate(d):
    # print(var)
            if var == inp:
        # print(en+1)
                f = data.iloc[[en]]['Контактный телефон']
                print(f)
            # if var != inp:
            #     print("ID СКУП в базе не найден")
            if inp == 'q':
                break
    except:
        print("ValueError: invalid literal for int() with base 10")
# print(d)