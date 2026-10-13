# Questão 5


idade = int(input("Digite a sua idade: "))
possui_vip = int(input("Possui convite VIP? (1 para Sim, 0 para Não): "))
e_organizador = int(input("É organizador(a) do evento? (1 para Sim, 0 para Não): "))


if (idade >= 18 and possui_vip >= 1) or e_organizador >= 1:
    print("Entrada PERMITIDA! Seja bem-vindo(a)")
else:
    print("Entrada NEGADA! Você não atende aos requisitos")
