def decimal_vers_basex(nb,facteur):
    output = []
    while nb//facteur > 0 and nb % facteur > 0:
        multiple = nb//facteur
        output.append(nb % facteur)
        nb = multiple
    output.append(nb % facteur)
    print(output)
    return(output)

def basex_vers_decimal(nb,facteur):
    nb = str(nb)
    output = 0
    for i in range(len(nb)):
        output += int(nb[-(i+1)])*(facteur**i)
    print(output)
    return(output)

a = input(" 1 : D => Bx\n 2 : Bx => D\n 3 : Ba => Bb\n  ")
if a == "1":
    nombre = int(input("Nombre : "))
    basex = int(input("BaseX : "))
    decimal_vers_basex(nombre,basex)
elif a == "2":
    nombre = int(input("Nombre : "))
    basex = int(input("BaseX : "))
    basex_vers_decimal(nombre,basex)
elif a == "3":
    nombre = int(input("Nombre : "))
    base_a = int(input("BaseA : "))
    base_b = int(input("BaseB : "))
    nombre = basex_vers_decimal(nombre,base_a)
    decimal_vers_basex(nombre,base_b)
