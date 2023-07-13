import pandas as pd
import classes as c
from menu import *
from time import sleep

l = c.lista_telefonica()

if __name__ == '__main__':
    while True:
        try:
            m = menu(
                'listar contatos',
                'Adicionar contato',
                'Excluir contato',
                'Buscar contato',
                'Salvar lista',
                'Carrregar lista',
                'Sair',
                title='Lista Telefonica'
                )

            match m.option():
                case 1:
                    m.line()
                    print(pd.DataFrame(l.lista))
                case 2:
                    m.line()
                    print("Adicionando novo contato")
                    l.add()
                case 3:
                    m.line()
                    print("Informe o nome que deseja remover")
                    l.remove(input('Nome: '))
                case 4:
                    m.line()
                    print("Informe o nome que deseja buscar em sua lista")
                    e = l.search(input('Nome: '))
                    match e:
                        case -1:
                            print('Não encontrado')
                        case _:
                            print(f"Encontrado na posição {e}")
                case 5:
                    m.line()
                    print('Informe o nome da lista para salva-la')
                    l.save(input('Nome da lista: '))
                case 6:
                    m.line()
                    print("Informe o nome do arquivo que deseja carregar")
                    l.read(input('Nome do arquivo: '))
                case 7:
                    print("Encerrando...")
                    sleep(2)
                    m.line()
                    break
            sleep(2)
        except KeyboardInterrupt:
            try:
                r = input("Deseja encerrar ? [S/N] ").strip().upper()[0]
                if r in 'S':
                    print("Encerrando...")
                    sleep(2)
                    menu.line()
                    break
            except Exception as erro:
                print(f"ERRO: {erro.__class__}")

        
