def verificar(palabra, aux): # se definio para ser mas claro y poder utilizar mas tarde 
    longitud = len(palabra) # len ya es un identificador de palabras lo cual me permite saber cuntas tengo almacenas en longitud 

    if longitud < 4:   # aqui empieza la magia donde longitud compara si es menor a 4 imprime hace falta letras 
        print( f"hace falta letras. solo tienes {longitud} letras.")
    elif 4 <= longitud <= 8:   #si longitud se encuentra entre 4 y 8 imprime correcto sino 
        print( "la palabra es correcta")
        aux=False 
    else: 
        print( f"sobra letras. tienes {longitud} letras.")
        return aux
aux = True
while aux ==True:
    palabra =input("indroduce una palabra  entre 4 y 8 palabra ")
    aux = verificar(palabra, aux)

#codigo para encontrar el cuadrante
# aqui definimos las cordenadas encontrar 
def encontrar(x, y):
    if x > 0 and y > 0:
        return "cudrante I"
    elif x < 0 and y > 0:
        return "cuadrante II"
    elif x < 0 and y < 0:
        return "cuadrante III"
    elif x > 0 and y < 0:
        return"cuadrante IV"
    elif x == 0 and y != 0:
        return"sobre el eje Y"
    elif y == 0 and x !=0:
        return "sobre el eje x"
    else:
        return "origen"

# pedidoms al usuario que ingrese un valor con numeros  y de esta forma nos arroje un valor del cudrante 
x = int(input("ingrese la cordenada X: ")) 
y = int(input("ingrese la cordenada Y: "))
cuadrante=encontrar(x , y)
print(f"La coordenada ({x} , {y}) se encuentra en {cuadrante} ") #aqui se imprime el resultado 

    



