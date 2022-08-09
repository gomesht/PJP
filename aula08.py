import requests
import json
while True:
    nome = input("Qual nome deseja pesquisar? ")
    if nome == "0":
        break
    response = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}').json()

    for i in range(len(response[0]['res'])):
        inter = response[0]['res'][i]['periodo'].replace("[","").replace(",", " a ")
        print(f"No periodo de {inter} a frequencia era {response[0]['res'][i]['frequencia']}")
    # [
    #     {
    #         'nome': 'HENRIQUE', 
    #         'sexo': None, 
    #         'localidade': 'BR', 
    #         'res': 
    #             [
    #                 {
    #                     'periodo': '1930[', 
    #                     'frequencia': 1776
    #                 }, 
    #                 {
    #                     'periodo': '[1930,1940[', 
    #                     'frequencia': 3493
    #                 }, 
    #                 {
    #                     'periodo': '[1940,1950[', 
    #                     'frequencia': 5166
    #                 }, 
    #                 {'periodo': '[1950,1960[', 'frequencia': 7307}, {'periodo': '[1960,1970[', 'frequencia': 10379}, {'periodo': '[1970,1980[', 'frequencia': 14189}, {'periodo': '[1980,1990[', 'frequencia': 34175}, {'periodo': '[1990,2000[', 'frequencia': 68395}, {'periodo': '[2000,2010[', 'frequencia': 83838}]}]