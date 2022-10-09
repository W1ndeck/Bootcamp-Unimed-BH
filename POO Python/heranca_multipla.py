# *args
# É usado para passar um lista de argumentos variável sem palavras-chave em forma de tupla, pois a função que o recebe não necessariamente saberá quantos argumentos serão passados.

# **kwargs
# Como a abreviação sugere, kwargs significa keyword arguments (argumentos de palavras chave). Ele permite passar um dicionário com inúmeras keys para a função.



class Animal:
    def __init__(self, nmr_patas):
        self.nmr_patas = nmr_patas

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Ornitorrinco(Mamifero, Ave):
    pass

ornitorrinco = Ornitorrinco(nmr_patas= 4, cor_bico="preto", cor_pelo="marrom")
print(ornitorrinco.cor_pelo)
print(ornitorrinco.nmr_patas) 