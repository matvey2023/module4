import requests

url="https://swapi.dev/api"
responce = requests.get(url).json()

people_api=responce.get('people')
planets_api=responce.get('planets')
starships_api=responce.get('starships')

# def check_people(url):
#     for i in range(1, 6):
#         responce = requests.get(f'{url}/{i}').json()
#         print(responce)
#
# def check_planets(url1):
#     diametrs_list=[]
#     for i in range(1, 6):
#         responce = requests.get(f'{url1}/{i}').json()
#         diametrs_list.append({responce.get("name") : responce.get("diameter")})
#     print(diametrs_list)

def check_starships(url1):
    speeds_list=[]
    for i in range(9, 14):
        responce = requests.get(f'{url1}/{i}').json()
        speeds_list.append({responce.get("name") : responce.get("max_atmosphering_speed")})
    print(speeds_list)

check_starships(starships_api)
# check_people(people_api)
