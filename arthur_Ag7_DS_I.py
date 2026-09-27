
TOTAL_ENTREVISTADOS = 10
qtd_excelente = 0
qtd_ruim = 0
contador = 1
print("--- PESQUISA DE SATISFAÇÃO TUDOWEB ---")
while contador <= TOTAL_ENTREVISTADOS:
    print(f"\nEntrevistado nº {contador}:")    
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    
    
    while True:
        print("Opinião sobre o atendimento:")
        print("1 - EXCELENTE")
        print("2 - RUIM")
        opiniao = input("Escolha uma opção (1 ou 2): ")
        

        if opiniao == '1':
            qtd_excelente += 1
            break
        elif opiniao == '2':
            qtd_ruim += 1
            break
        else:
            print("Opção inválida! Por favor, digite 1, 2 ou 3.\n")
            
    contador += 1


print("\n" + "="*30)
print("       Resultado da pesquisa       ")
print("="*30)
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"c) Quantidade de respostas 'RUIM': {qtd_ruim}")
print(f"Total de pessoas entrevistadas: {TOTAL_ENTREVISTADOS}")
print("="*30)
