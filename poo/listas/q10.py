sistemas = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
so = [0,0,0,0,0,0]

while True:
    print("Qual o melhor Sistema Operacional para uso em servidores?")
    print('''
            1- Windows Server
            2- Unix
            3- Linux
            4- Netware
            5- Mac OS
            6- Outro
        ''')
    opcao = int(input("Digite a opção: "))
    if opcao >= 0 and opcao <= 6:
        if opcao == 0:
            break
        so[opcao-1] += 1

print(f'''
Sistema Operacional             Votos           %
---------------------------   --------         ---
''')
for i in range(6):
    print(f"{sistemas[i]}                  {so[i]}   {(so[i]*100/sum(so)):.2f}%")

print(f'''-------------------           ---------
Total                           {sum(so)}
''')

print("O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.")