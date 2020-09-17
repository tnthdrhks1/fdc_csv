import urllib.request
import json
import pandas as pd

f = open('ingredients_number.csv', 'r', encoding='utf-8-sig')
name1 = []
list1 = []
phk = f.read()
name0 = phk.split('\n')

#print(list1)
f.close

name_list = []
number_list = []
kcal_list = []
realname_list = []

# 여기까지 foundataion food 번호 가져오기

i = 0
j = 0

give_null = None

food_list = []
client_key = 'Q50q1HtoFam9uDbFg0WCZMdSefalwC7ITd7NHcKT'

encText = urllib.parse.quote_plus("Q50q1HtoFam9uDbFg0WCZMdSefalwC7ITd7NHcKT")

with open('food_list_20200906.csv', 'w', encoding='utf-8-sig') as file:

    for num in range(174657 , 175305):
        #175305 가 끝
        naver_url = 'https://api.nal.usda.gov/fdc/v1/food/{0}?api_key='.format(num) + encText
        food_list.append(naver_url)

        request = urllib.request.Request(food_list[num-174657])
        request.add_header("X-Naver-Client-Id",client_key)

        response = urllib.request.urlopen(request)

        rescode = response.getcode()

        if(rescode == 200):
            response_body = response.read()
            data = json.loads(response_body)

            realname = data['description']
            realname_list.append(realname)
            
            for i in range (1000):
                try:
                    name = data['foodNutrients'][i]['nutrient']['name']
                    number = data['foodNutrients'][i]['nutrient']['number']
                    kcal = data['foodNutrients'][i]['amount']
                    food_ca = data['foodCategory']['description']

                    name_list.append(name)
                    number_list.append(number)
                    kcal_list.append(kcal)

                    
            
                except:
                    pass
            # if(food_ca == 'Vegetables and Vegetable Products'):  
            print("재료 이름 : {0}".format(realname))
                    
            file.write('{0}\n'.format(realname))

            # for q in range(len(number_list)-1):
            #     for p in range(len(name0)-1):
            #         if (int(number_list[q]) == int(name0[p])): 
            #             file.write('{0},'.format(name_list[q]))
            #             break

            for q in range(len(number_list)-1):
                for p in range(len(name0)-1):
                    if (int(number_list[q]) == int(name0[p])): 
                        file.write('{0},'.format(kcal_list[q]))
                        break
            file.write('\n')    

            name_list = []
            number_list = []
            kcal_list = []      