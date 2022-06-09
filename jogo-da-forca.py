from random import randint

def construir_boneco(erro=0):
    if erro == 1:
        print(''' ______
 |     |
 |     O
 |    
 |    
 |    
_|_   ''')
    if erro == 2:
        print(''' ______
 |     |
 |     O
 |     |
 |     |
 |    
_|_   ''')
    if erro == 3:
        print(''' ______
 |     |
 |     O
 |    /|
 |     |
 |    
_|_   ''')
    if erro == 4:
        print(''' ______
 |     |
 |     O
 |    /|\\
 |     |
 |    
_|_   ''')
    if erro == 5:
        print(''' ______
 |     |
 |     O
 |    /|\\
 |     |
 |    /
_|_   ''')
    if erro == 6:
        print(''' ______
 |     |
 |     O
 |    /|\\
 |     |
 |    / \\
_|_   ''')

def definir_palavra():
    palavras = ["Cereal","Classe","Submergir","Holanda","Aplauso","Transporte","Nuclear","Kilos","Homens","Eclipse"]
    palavra_escolhida = palavras[randint(0, len(palavras))]
    return palavra_escolhida, len(palavra_escolhida)

def printar_underline(tamanho_palavra):
    print('_ '*tamanho_palavra)

chance = 0
while chance < 6:
    print(''' ______
 |     |
 |     
 |    
 |     
 |    
_|_   ''')
    
construir_boneco(3)
define_palavra()

