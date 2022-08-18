import requests
def main():
    try:
        pokemon = escolha_pokemon()
        infos = importa_infos(pokemon)
        for i in infos:
            print(i ,infos[i])
    except:
        print("Não enconterei informações sobre esse Pokémon...\nConfira se digitou um valór válido")
def escolha_pokemon(): 
    return input("Qual pokemon você deseja: ")

def importa_infos(p):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{p}/").json()
    nome = response["name"]
    peso = response["weight"]
    tamanho = response["height"]
    tipos = []
    for i in range(len(response["types"])):
        tipos.append(response["types"][i]["type"]["name"])
    imagem = response["sprites"]["versions"]["generation-v"]["black-white"]["animated"]["front_default"]
    return{"Nome:":nome, "Peso:":peso, "Tamanho:":tamanho,"Tipos:":tipos,"Imagem:":imagem}

main()