simbolos = ['1', '2', '3']
estados = [
    '0',
    'A1', 'A2', 'A3',
    'B2', 'B3', 'B4', 'B5', 'B6',
    'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10'
    ]
matrizTrans = [
    ['A1', 'A2', 'A3'],
    ['B2', 'B3', 'B4'],
    ['B3', 'B4', 'B5'],
    ['B4', 'B5', 'B6'],
    ['C3', 'C4', 'C5'],
    ['C4', 'C5', 'C6'],
    ['C5', 'C6', 'C7'],
    ['C6', 'C7', 'C8'],
    ['C7', 'C8', 'C9'],
    ]
estadoInicial = '0'
estadosFinales = ['C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10']

def chatbot(cadena):
    estado = estadoInicial
    for c in cadena:
        if c not in simbolos:
            return None
        
        estado = matrizTrans[estados.index(estado)][simbolos.index(c)]
        
        if estado in estadosFinales:
            return estado

preguntas = [
    'A) Ingresa tu estado de ánimo:\n1: Triste\n2: Tranquilo\n3: Feliz\n',
    '\nB) Ingresa tu género favorito:\n1: Clásico\n2: Electrónico\n3: Rock\n',
    '\nC) Ingresa tu actividad:\n1: Leer\n2: Caminar\n3: Ejercicio\n',
]
respuestas = []
canciones = [
    'Spells - acloudyskye',
    'Burn - Tristam',
    'Blue Jeans - Lana del Rey',
    'Summer - Imagine Dragons',
    'Plastic Hearts - Miley Cyrus',
    'Exit Music (For A Film) - Radiohead',
    'Knights of Cydonia - Muse',
    ]

for p in preguntas:
    seleccion = input(p)
    while seleccion not in ['1', '2', '3']:
        seleccion = input(p)
    respuestas.append(seleccion)
    
nivel = chatbot(respuestas)[1]

print('\nTu canción a escuchar es:')
print(canciones[int(nivel)-3])