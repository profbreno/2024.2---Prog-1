def balanca(kg):
    return 50.00*kg

kg = float(input("Digite o peso em kg: "))
print(f"Seu prato pesa {kg}kg")
print(f"O valor a pagar é R${balanca(kg):.2f}")