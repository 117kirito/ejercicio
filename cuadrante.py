def verificar(palabra, aux): # se definio para ser mas claro y poder utilizar mas tarde 
    longitud = len(palabra) # len ya es un identificador de palabras lo cual me permite saber cuntas tengo almacenas en longitud 

    if longitud < 4:   # aqui empieza la magia donde longitud compara si es menor a 4 imprime hace falta letras 
        print( f"hace falta letras. solo tienes {longitud} letras.")
    elif 4 <= longitud <= 8:   #si longitud se encuentra entre 4 y 8 imprime correcto sino 
        print( "la palabra es correcta")
        aux=False # cambia aux a fa
    else: 
        print( f"sobra letras. tienes {longitud} letras.")
        return aux
    
aux = True
while aux ==True:
    palabra =input("indroduce una palabra  entre 4 y 8 palabra ")
    aux = verificar(palabra, aux)


    x = int(input("ingrese la cordenada X: "))

