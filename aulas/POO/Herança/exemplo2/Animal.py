# classe PAI

class Animal:()

def _init__(self,tipo,idade,regiao):

    self.tipo = tipo= tipo # protected
    self.idade = idade = idade # protected
    self.regiao = regiao = regiao # protected

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self,tipo):
        self._tipo = tipo
    @property
    def idade (self):
        return self._idade
    @idade.setter
    def idade(self,idade):
        self._idade = idade
    @property
    def regiao (self):
        return self._regiao

    def comer(self):# publicos
        print(f'o aniamal{self,_tipo} está comodo.")'

    def dormir(self):# publicos
        print(f'o animal {selt,_tipo})
