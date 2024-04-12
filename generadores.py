#permite extraer valores de una fucion y almacenarlos de uno en uno en objetos iterables (que se pueden recorrer) sin la necesidad de almacenarlos todoz a la vez en la memoria

def mut7(lim, base):
    contador = 1
    list_base = []
    
    while contador <= lim:
        list_base.append(contador*base)
        contador = contador + 1
    return list_base
        
base=int(input("Que base deseas => "))
lim = int(input("Cual es el limite => "))

print(mut7(lim, base))

def gen_mul_7(limit):
    num = 1
    while num <= limit:
        yield num *7
        num = num + 1
        
obt_7 = gen_mul_7(11)

print(list(obt_7))
        