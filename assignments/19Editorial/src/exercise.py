def main():
    # escribe tu código abajo de esta línea
    palabras = int(input("Dame el número de palabras: "))
    costo = ((palabras // 475) + 1) * 54
    print("El costo de la publicación es:", costo)


if __name__ == '__main__':
    main()
