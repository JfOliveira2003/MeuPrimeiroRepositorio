#!/usr/bin/python3

print('Hello world"')
k = int(input('Digite sua idade: '))
if k >= 18:
	print('Parabéns! Você já pode ser preso.')
else:
	print('que?')
print('Você nasceu em: ', end="")
print( 2023 - k)
