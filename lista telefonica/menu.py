class menu:
    def __init__(self, *opc, title):
        self.line()
        print(title.center(40))
        self.options = len(opc)
        for n, o in enumerate(opc):
            print(f'{n + 1} - {o}')
        
    def option(self):
        while True:
            try:
                opt = int(input('Sua opção: '))
                if opt > self.options or opt <= 0:
                    raise IndexError
            except (ValueError, TypeError):
                print('Opção inválida!')
            except IndexError:
                print(f"Opção inválida! escolha uma opção entre 1 e {self.options}")
            else:
                return opt

    @staticmethod
    def line():
        print('-' * 40)
