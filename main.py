#Programa para imprimir número impar ou par
numero = int(input("Digite um número: "))
if numero % 2 == 0:
  print("O número é par")
else:
  print("O número é impar")

#Programa para receber dois números e imprimir o maior
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
if numero1 > numero2:
  print("O maior número é:", numero1)
else:
  print("O maior número é:", numero2)

#Programa para receber dois números e dividir, caso o segundo número seja 0 avisar erro
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número:"))
if numero2 == 0:
  print("Erro: Divisão por zero")
else:
  divisao = numero1 / numero2
  print("A divisão é:", divisao)

#Programa para receber três números e imprimir o menor
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segndo número: "))
numero3 = int(input("Digite o terceiro número: "))
if numero1 < numero2 and numero1 < numero3:
  print("O menor número é:", numero1)
else:
  if numero2 < numero1 and numero2 < numero3:
    print("O menor número é:", numero2)
  else:
    print("O menor número é:", numero3)

#Programa para receber preço e imprimir mensagem de acordo com o preço
valor = float(input("Digite o valor do produto: "))
if valor <= 0:
  print("Preço inválido")
else:
  if valor <= 30:
    print("Preço baixo")
  else:
    if valor > 30 and valor <= 50:
      print("Preço médio")
    else:
      print("Preço alto")

#Programa para aplicar taxa de juros de acordo com o preço
valor = float(input("Digite o valor do produto: "))
if valor < 0:
    print("Valor inválido")
else: 
    if valor < 100:
        valor *= 1.1
    elif 100 <= valor < 300:
        valor *= 1.2
    elif 300 <= valor < 1000:
        valor *= 1.5
    print(valor)

#Programa para imprimir se ano é bissexto
ano = int(input("Digite o ano: "))
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(ano, "é bissexto")
else:
    print(ano, "não é bissexto")

print("Programa que exibe menu de calculadora e realize a operação escolhida")
print("Menu de opções")
print("Digite 1 para somar dois valores")
print("Digite 2 para subtrair dois valores")
print("Digite 3 para multiplicar dois valores")
print("Digite 4 para dividir dois valores")
print("Digite 5 para realizar uma potência entre dois valores")
print("Digite 6 para realizar uma radiciação entre dois valores")
print("Digite qualquer outro número para sair")
opcao = int(input("Escolha uma opção: "))
if opcao in range(1, 7):
      valor1 = float(input("Digite o primeiro valor: "))
      valor2 = float(input("Digite o segundo valor: "))
      if opcao == 1:
          resultado = valor1 + valor2
          print("A soma é:", resultado)
      elif opcao == 2:
          resultado = valor1 - valor2
          print("A subtração é:", resultado)
      elif opcao == 3:
          resultado = valor1 * valor2
          print("A multiplicação é:", resultado)
      elif opcao == 4:
          if valor2 != 0:
              resultado = valor1 / valor2
              print("A divisão é:", resultado)
          else:
              print("Erro: divisão por zero!")
      elif opcao == 5:
          resultado = valor1 ** valor2
          print("A potência é:", resultado)
      elif opcao == 6:
          if valor1 >= 0:
              resultado = valor1 ** (1 / valor2)
              print("A radiciação é:", resultado)
          else:
              print("Erro: valor base negativo para radiciação!")
else:
      print("Opção inválida. Encerrando o programa.")