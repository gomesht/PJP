import sqlite3
from classes import Cardapio
cardapio = Cardapio()
while True:
    op = input("O que deseja fazer:\n1 - Ver cardápio\n2 - Adicionar item ao cardápio\n3 - Remover item do Cardápio\n4 - Editar item do cardápio\n5 - Sair\n")
    match op:
        case "1":
            cardapio.verItens()
            
        case "2":
            cardapio.addItem()
            
        case "3":
            cardapio.rmItem()
            
        case "4":
            cardapio.alterarItem()
            
        case "5":
            break
