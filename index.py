# Matriz mutante
adn_mutante = [
    "ATGCGA",
    "CAGTGC",
    "TTATGT",
    "AGAAGG",
    "CCCCTA",
    "TCACTG"
]

#Matriz no mutante
adn_no_mutante = [
    "ATGCGA",
    "CAGTGC",
    "TTATTT",
    "AGACGG",
    "GCGTCA",
    "TCACTG",
]

# Llenado de matriz
def llenar_matriz ():
    matriz_adn = []
    
    for i in range(6):
        fila_valida = False
        
        while not fila_valida:
            fila = input(f"Ingrese 6 caracteres para la fila {i + 1} (solo con caracteres 'A,T,G o C): ").upper()
            
            if len(fila) == 6 and all(caracter in 'ATCG' for caracter in fila):
                fila_valida = True
            else:
                print("Error: la fila debe contener 6 caracteres y deben ser 'A, T, C o G")
        
        matriz_adn.append(list(fila))
        
    return matriz_adn

def mostrar_matriz (matriz):
    for fila in matriz:
        print(''.join(fila))

def es_mutante (matriz):
    largo_matriz = len(matriz)
    # Verificacion horizontal y vertical
    for i in range(largo_matriz):
        for j in range(largo_matriz - 3):
            if len(set(matriz[i][j:j + 4])) == 1:
                return True
            
            if i + 3 < largo_matriz and matriz[i][j] == matriz[i+1][j] == matriz[i+2][j] == matriz[i+3][j]:
                return True
    
    # Verificacion oblicua 
    for i in range(largo_matriz - 3):
        for j in range(largo_matriz - 3):
            if len(set(matriz[i + k][j + k] for k in range(4))) == 1:
                return True
                
    return False

# matriz_creada = llenar_matriz()

print("Matriz creada por el usuario: ")
mostrar_matriz(adn_mutante)

if es_mutante(adn_mutante):
    print("Es mutante")
else:
    print("No es mutante")