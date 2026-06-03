historico_principal = []
historico_secundaria = []

continuar = "sim"

while continuar == "sim":

    ambulancia = input("Há alguma ambulância na via? (sim/não): ").lower()

    if ambulancia == "sim":
        print("Em qual via está a ambulância?")
        print("1 - Via principal")
        print("2 - Via secundária")

        via_ambulancia = int(input("Escolha uma opção: "))

    qtd_secundaria = int(input("Digite a quantidade de carros na via secundária: "))
    qtd_principal = int(input("Digite a quantidade de carros na via principal: "))

    historico_principal.append(qtd_principal)
    historico_secundaria.append(qtd_secundaria)

    if ambulancia == "sim":

        if via_ambulancia == 1:

            tempo_principal = 30
            tempo_secundaria = 10

            print("Prioridade para ambulância na via principal.")

        elif via_ambulancia == 2:

            tempo_principal = 10
            tempo_secundaria = 30

            print("Prioridade para ambulância na via secundária.")

        else:

            tempo_principal = 20
            tempo_secundaria = 20

            print("Opção inválida.")

    elif qtd_principal > qtd_secundaria:

        tempo_principal = 30
        tempo_secundaria = 10

    elif qtd_secundaria > qtd_principal:

        tempo_principal = 10
        tempo_secundaria = 30

    else:

        tempo_principal = 20
        tempo_secundaria = 20

    print(f"Tempo da via principal: {tempo_principal} segundos")
    print(f"Tempo da via secundária: {tempo_secundaria} segundos")

    falha = input("O semáforo está funcionando corretamente? (sim/não): ").lower()

    if falha == "sim":
        print("O semáforo está funcionando normalmente.")

    else:

        print("Tipos de falha:")
        print("1 - Lâmpada queimada")
        print("2 - Falta de energia")
        print("3 - Cabo de energia rompido")

        opcao_falha = int(input("Escolha uma opção: "))

        if opcao_falha == 1:
            print("Lâmpada queimada")

        elif opcao_falha == 2:
            print("Falta de energia")

        elif opcao_falha == 3:
            print("Cabo de energia rompido")

        else:
            print("Falha não identificada, vamos acionar a equipe de manutenção.")

    continuar = input("\nDeseja realizar uma nova leitura? (sim/não): ").lower()

print("\nHistórico da via principal:")
for valor in historico_principal:
    print(valor)

print("\nHistórico da via secundária:")
for valor in historico_secundaria:
    print(valor)

print("\nSistema encerrado.")