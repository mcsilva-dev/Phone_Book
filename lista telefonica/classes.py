import string
import pandas as pd


class lista_telefonica:
    def __init__(self):
        self.lista = {
            'Name': [],
            'Number': []
        }

    def __len__(self):
        return len(self.lista['Name'])

    def __iter__(self):
        return iter(self.lista.items())
    
    def listar(self):
        return pd.DataFrame(self.lista)

    def add(self):
        while True:
            try:
                name = ' '.join(input('Nome: ').title().strip().split())
                if name == '' or name == None:
                    raise ValueError
                for l in ''.join(name.replace(' ', '')):
                    if l in string.digits or l in string.punctuation:
                        raise TypeError
            except TypeError:
                print('ERRO: O nome deve conter apenas letras')
            except ValueError:
                print('ERRO: O nome não pode ser vazio ou None')
            except Exception as erro:
                print(f'ERRO: {erro.__class__}')
            else:
                break
        while True:
            try:
                number = ''.join(input('Telefone: ').strip().split())
                if number == '':
                    raise ValueError
                elif len(number) < 9:
                    raise IndexError
                for n in number:
                    if n in string.ascii_letters or n in string.punctuation:
                        raise TypeError
            except (ValueError, TypeError):
                print('ERRO: o número deve conter somente digitos de 0 a 9')
            except IndexError:
                print('ERRO: o número deve conter 9 caracteres.')
            except Exception as erro:
                print(f'ERRO: {erro.__class__}')
            else:
                break
        match self.search(name):
            case -1:
                self.lista['Name'].append(name)
                self.lista['Number'].append(number)
                print(f"{name} adicionado com sucesso!")
            case _:
                print(f"{name} já existe na lista")

    def save(self, text):
        with open(text, 'w', encoding='utf-8') as arquivo:
            c = 0
            for k in self.lista.keys():
                if c < len(self.lista.keys()) - 1:
                    arquivo.write(f'{k},')
                else:
                    arquivo.write(f'{k}\n')
                c += 1
            for v in range(0, len(self.lista['Name'])):
                arquivo.write(f'{self.lista["Name"][v]},{self.lista["Number"][v]}\n')

    def read(self, text):
        with open(text, 'r', encoding='utf-8') as arquivo:
            lines = len(arquivo.readlines())
        with open(text, 'r', encoding='utf-8') as arquivo:
            keys = arquivo.readline().replace('\n', '').split(',')
            for k in keys:
                self.lista[k] = []
            p = []
            while lines - 1 > 0:
                p += arquivo.readline().replace('\n', '').split(',')
                lines -= 1
            for n in range(0, len(p)):
                match n % 2:
                    case 0:
                        self.lista[keys[0]].append(p[n])
                    case _:
                        self.lista[keys[1]].append(p[n])
        print(f"{text} carregado com sucesso.")

    def search(self, nome):
        try:
            return self.lista['Name'].index(nome)
        except ValueError:
            return -1

    def remove(self, nome):
        index = self.search(nome)
        match index != -1:
            case True:
                while True:
                    q = input(f"Deseja remover {self.lista['Name'][index]}? [S/N]").strip().upper()[0]
                    match q:
                        case 'S':
                            del self.lista['Name'][index]
                            del self.lista['Number'][index]
                            break
                        case 'N':
                            break
                        case _:
                            print('Opção inválida! Digite S ou N!')
            case _:
                print(f"{nome} não foi encontrado na lista.")


