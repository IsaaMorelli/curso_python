"""
fatiamento de strings
 012345
 Hello!
-654321
Fatiamento(I:F:P)
I = inicio
F = fim
P = passo
função len (conta o numero de caracteres)
"""
var = 'Hello!'
var2 = 'Maybe'
print(var[0:2] + var2[2] + var[5])
print(len(var), len(var2))

#inverter palavra
print(var[ : :-1])
print(var2[ : :-1])