class Texto():
    
    linhas = []
    __dock = []
    __dock_n = []
    __docker = []
    __taxo = []
    __resultado = []
    
    col = 0
    
    def __init__(self):
        file = open('Arquivos/portalbio_export_16-10-2019-14-39-54.csv', 'r')
        self.linhas = file.readlines()
    
    def construir(self, lines):
        self.__dock = [[item for item in itens.split(',')]for itens in lines]
        return self.__dock
        
    def count_nulls(self, lista):
      
        def funcao(texto):
            return True if texto == "Sem Informações" or texto == " " else False
        colunas_vazias = [sum([funcao(lista[linha][coluna]) for linha in range(len(lista))]) for coluna in range(len(lista[0]))]
        return colunas_vazias
    
    def media_nulls(self, lista):
        
        a = lambda x: x / (len(self.__dock)-1)
        return [a(item) for item in lista]
    
    def taxonom(self):
        
        for item in self.__dock:
            col = len(item)
            
        count=0
        for i in range(0, col):
            if self.__dock[0][i] == 'Filo':
                count = i
                
        def testar(teste):
            return False if teste == "Sem Informações" or teste == " " else True
        novas_colunas = [sum([testar(self.__dock[linha][coluna]) for coluna in range(count, count+6)]) for linha in range(len(self.__dock))]
        
        self.__resultado.append(novas_colunas)
        return self.__resultado
