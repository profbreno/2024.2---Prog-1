from Lutador import Lutador

ryu = Lutador("Ryu", 100, 10)
bison = Lutador("Bison", 100, 12)

for _ in range(3):
    ryu.aplicarGolpe(bison)

print(bison.energia)

for _ in range(10):
    bison.aplicarGolpe(ryu)

print(ryu.energia)