import requests

while True:
    cidade = input("Digite a cidade: ")
    if cidade == "0":
        break
   
    response = requests.get(f"https://weather.contrateumdev.com.br/api/weather/city/?city={cidade}").json()
    temperatura = response["main"]["temp"]
    minima = response["main"]["temp_min"]
    maxima = response["main"]["temp_max"]
    descri = response["weather"][0]["description"]
    vento = response["wind"]["speed"]
    print(f"O tempo em {cidade} está: {descri}\nTemperatura: {temperatura}\nMax: {maxima}\nMin: {minima}\nVelocidade do vento: {vento} ")