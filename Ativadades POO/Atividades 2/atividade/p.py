class produto :
    def __init__(self, nome,prço, quantidade_de_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade_de_estoque

        @property
        def nome (self ):
            return self.__nome

        @nome.setter