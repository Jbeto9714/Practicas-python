
texto = "Bienvenidos al canal"

print(texto)

print(texto.lower())
print(texto.upper())
print(texto.title())
print(texto.find("al"))
print(texto.count("e"))

textofinal = texto.replace("e", "3")
print(textofinal)

valor = texto.isnumeric()
print(valor)

cadenaseparada = texto.split(" ")
print(cadenaseparada)
