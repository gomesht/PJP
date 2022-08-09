# x = "python"

# print(x.isnumeric())

# lista=["1","2"]

# print(type(int(lista[0])))

#x = "20"
# y = "15"
# print(eval(f"{y}+{x}"))
#print(x.isnumeric())
# cpf = "11111111111"
# mult=0
# for i in range (2,11):
#     mult += int(cpf[i])*(10-(i-2))
#     res = (mult*10)%11
# print(mult,res)
# print(540%11, 540//11)
# dicionario = {
#     "id": 1, 
#     "nome": "roberto",
#     "compras": [
#         "notebook",
#         "mouse",
#         "teclado"
#     ]
# }
# print (dicionario["compras"][0])
import requests
import json

response = requests.get('https://servicodados.ibge.gov.br/api/v2/censos/nomes/Henrique').json()
print(json.dumps(response, indent=4))
o = response
for results in o["res"]:
    print(results["periodo"])

# [
#     {
#         "nome": "HENRIQUE",
#         "sexo": null,
#         "localidade": "BR",
#         "res": [
#             {
#                 "periodo": "1930[",
#                 "frequencia": 1776
#             },
#             {
#                 "periodo": "[1930,1940[",
#                 "frequencia": 3493
#             },
#             {
#                 "periodo": "[1940,1950[",
#                 "frequencia": 5166
#             },
#             {
#                 "periodo": "[1950,1960[",
#                 "frequencia": 7307
#             },
#             {
#                 "periodo": "[1960,1970[",
#                 "frequencia": 10379
#             },
#             {
#                 "periodo": "[1970,1980[",
#                 "frequencia": 14189
#             },
#             {
#                 "periodo": "[1980,1990[",
#                 "frequencia": 34175
#             },
#             {
#                 "periodo": "[1990,2000[",
#                 "frequencia": 68395
#             },
#             {
#                 "periodo": "[2000,2010[",
#                 "frequencia": 83838
#             }
#         ]
#     }
# ]