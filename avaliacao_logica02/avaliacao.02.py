# [LP-A02] Escreva um programa em python que pergunte ao usuário a velocidade de um carro. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.

velocidade = float(input("Digite a velocidade do carro: "))

if velocidade > 80:
    print(f"A sua velocidade era de {velocidade}km/h, e ultrapassou o limite de 80km/g da via, você foi multado.")
    print(f"Você ira pagar uma mulda de R${(velocidade - 80)*20 :.2f}")

else:
    print("Parabéns, você não ultrapassou a velocidade limite de 80km/h")