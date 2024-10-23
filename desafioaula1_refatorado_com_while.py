#Escreva um programa que o usuario inputa seu nome, seu salário e o % do seu bonus e é retornado uma saudação, o valor do bonus
#Salario*bonus + 1000
#Pensar nos erros possíveis e corrigí-los


CONSTANTE_BONUS = 1000

#Variáveis de validação do fluxo while
nome_valido = False
salario_valido = False
nome_valido = False
bonus_valido = False


#Input nome
while nome_valido is not True:
    try:
        nome = input('Insira seu primeiro nome ')

        if len(nome)==0: #verifica se o input está em branco
            print('Você não digitou seu nome')

        elif nome.isspace():
            print('Você digitou só espaço')

        elif not nome.isalpha(): #verifica se o input é composto por letras e números
            print('Digite apenas letras')
        
        else:
            nome_valido = True
            print('Nome inserido corretamente')
    except ValueError as e:
        print(e)
    
#input salario
while salario_valido is not True:
    try:
        salario = input('Insira seu salário ')
        salario = float(salario)
        salario_valido = True
        print(f'O salario inserido é igual a {salario:.2f}')
    except (ValueError, TypeError):
        if ',' in salario or ' ' in salario:
            salario = salario.replace(',', '.').replace(' ','')
            try:
                salario = float(salario)
                salario_valido = True
                print(f'O salario inserido é igual a {salario:.2f}')
            except (ValueError, TypeError) as e:
                print(e)
                print('Insira um salário válido.')
        else: print('Insira um salário válido.')
 
#input percentual_bonus
while bonus_valido is not True:
    try:
        percentual_bonus = input('Insira o percentual do seu bonus ')
        percentual_bonus = float(percentual_bonus)
        bonus_valido = True
        print(f'O bonus inserido é igual a {percentual_bonus:.2f}')
    except:
        #verificação se o número foi inserido com vírgula
        if ',' in percentual_bonus or ' ' in percentual_bonus:
            percentual_bonus = percentual_bonus.replace(',','.').replace(' ','')
            try:
                percentual_bonus = float(percentual_bonus)
                bonus_valido = True
                print(f'O bonus inserido é igual a {percentual_bonus:.2f}')
            except (ValueError, TypeError) as e:
                print(e)
                print('Bonus inserido inválido, insira novamente.')
        else:
            print('Bonus inserido inválido, insira novamente.')
        
#calculo do total recebido
calculo = (salario * percentual_bonus)+CONSTANTE_BONUS #substituindo o 1000 hard code por uma variável, melhor a longo prazo
remuneracao_total = salario+calculo
print(f'Olá {nome}, o total de bonus recebido é de {calculo:.2f} e o total recebido no mês é de {remuneracao_total:.2f}')
#o f dentro do print permite printar textos e números/variáveis juntos, do contrário, retornaria um erro. Perceba que a sintaxe muda!!

# CORREÇÃO FEITA NO CHAT GPT, MAIS SUCINTA

# Input salario
# try:
#     salario = input('Insira seu salário: ').strip()  # Remover espaços em branco ao redor
#     if ',' in salario:
#         salario = salario.replace(',', '.')  # Correção da vírgula para ponto
    
#     # Tente converter o salário para float
#     salario_float = float(salario)
#     print(f'Seu salário é: {salario_float}')  # Exibe o salário convertido
# except ValueError:  # Captura apenas erros de conversão de valor
#     print('Entrada inválida. Por favor, insira um número válido.')
