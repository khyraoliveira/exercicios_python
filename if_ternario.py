# Permite escrever uma condição em uma única linha!
# Ele é composto por três partes:
# A primeira parte é o retorno caso a expressão retorne verdadeiro;
# A segunda parte é a expressão lógica;
# E a terceira parte é o retorno caso a expressão não seja atendida.

saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")