from paciente import Paciente, Anamnese

def main():
    paciente1 = Paciente("João", 30, "Masculino")
    anamnese1 = Anamnese("2022-01-01", "Dor de cabeça")
    anamnese2 = Anamnese("2022-02-01", "Febre")

    paciente1.adicionar_anamnese(anamnese1)
    paciente1.adicionar_anamnese(anamnese2)

    print(paciente1.nome)
    print(paciente1.listar_anamneses())
    
if __name__ == "__main__":
    main()