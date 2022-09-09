import sqlite3
from classes import Agenda
agenda = Agenda()
while True:
    op = input("O que deseja fazer:\n1 - Ver contatos\n2 - Adicionar contato\n3 - Remover contato\n4 - Editar contato\n5 - Sair\n")
    match op:
        case "1":
            agenda.verItens()
            
        case "2":
            agenda.addItem()
            
        case "3":
            agenda.rmItem()
            
        case "4":
            agenda.alterarItem()
            
        case "5":
            break