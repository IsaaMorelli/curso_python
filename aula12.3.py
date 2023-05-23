#formatação
name = 'matheus'
height = 1.82
weight = 82
imc = weight /(height * height)
linha1 = f"{name} is {height:.2f} tall, weights {weight}"
linha2 = f"and your IMC is {imc:.2f}"
print(linha1, end = " ")
print(linha2)