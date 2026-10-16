##Atividade 12

Pão = 5.00
meu_dinheiro = int(input("Quanto dinheiro você tem na carteira: "))

if meu_dinheiro >= Pão:

    sobra = meu_dinheiro - Pão
    print("Você comprou o pão! E sobraram", sobra, "reais.")
else:
    print("Dinheiro insuficiente.")