
#Aqui começão as boas vindas
print('-'*100)
print('|                        Bem-vindo a Sorveteria do Jonathan Santos de Oliveira')
print('-'*100)
print('          | Nº DE BOLAS | SABOR TRADICIONAL (TR) | SABOR PREMIUM (PR) | SABOR ESPECIAL (ES) |')
print('          |       1     |         R$ 6,00        |      R$ 7,00       |        R$ 8,00      |')
print('          |       2     |         R$ 11,00       |      R$ 13,00      |        R$ 15,00     |')
print('          |       3     |         R$ 15,00       |      R$ 18,00      |        R$ 21,00     |')
print('-'*100)

#Valor Bolas de Sabor Tradicional
SaborTR = 6
SaborTR1 = 11
SaborTR2 = 15

#Valor Bolas de Sabor Premium
SaborPR = 7
SaborPR1 = 13
SaborPR2 = 18

#Valor Bolas de Sabor Especial
SaborES = 8
SaborES1 = 15
SaborES2 = 21

#Armazenamento de dados
Calculo1 = 0
Calculo2 = 0
Calculo3 = 0
Calculo4 = 0
Calculo5 = 0
Calculo6 = 0
Calculo7 = 0
Calculo8 = 0
Calculo9 = 0

#Aqui começa a lógica
while True:
        EscolhaSabor = str(input('Entre com o sabor desejado TR/PR/ES: '))
# sabor Tradicional
        if EscolhaSabor.lower() == 'tr':
                numeroDeBolasTR = int(input('\nVocê escolheu sorvete sabor tradicional \nEntre com numero de bolas de sorvete desejado (1/2/3): ' ))
# uma bola de Sorvete
                if numeroDeBolasTR == 1:
                        Calculo1 += SaborTR
                        Decisao = input('\nvocê pediu 1 bola de sorvete no sabor Tradicional: R$ {:.2f} \nDeseja mais algum sorvete, digite "S" para Sim, e "N" para Não: '.format(
                                        SaborTR))
                        if Decisao.lower() == "s":
                                continue

                        elif Decisao.lower() == "n":
                                break
                        else:
                                print('Digite somente S para sim e N para não')
# Duas bolas de sorvete
                elif numeroDeBolasTR == 2:
                        Calculo2 += SaborTR1
                        Decisao =input('\nvocê pediu 2 bolas de sorvete no sabor Tradicional: R$ {:.2f} \nDeseja mais algum sorvete, digite S "Sim", e N para "Não"'.format(
                                        SaborTR1))
                        if Decisao.lower() == "s":
                                continue

                        elif Decisao.lower() == "n":
                                break
                        else:
                                print('Digite somente Y para sim e N para não')
# Tres bolas de sorvete
                elif numeroDeBolasTR == 3:
                        Calculo3 += SaborTR2
                        Decisao = input('\nvocê pediu 3 bolas de sorvete no sabor Tradicional: R$ {:.2f} \nDeseja mais algum sorvete, digite S "Sim", e N para "Não"'.format(
                                        SaborTR2))
                        if Decisao.lower() == "s":
                                continue

                        elif Decisao.lower() == "n":
                                break
                        else:
                                print('Digite somente Y para sim e N para não')
                else:
                        print('\nNº de bolas Errado')
                        print('digite um valor entre 1 e 3 bolas de sorvete: \n')
                        continue

# sabor Premium
        elif EscolhaSabor.lower() == 'pr':
                numeroDeBolasPR = int(input('Você escolheu sorvete sabor Premium\nEntre com numero de bolas de sorvete desejado (1/2/3): '))
# uma bola de Sorvete
                if numeroDeBolasPR == 1:
                        Calculo4 += SaborPR
                        Decisao = input('\nvocê pediu 1 bola de sorvete no sabor Premium: R$ {:.2f} \nDeseja mais algum sorvete, digite "S" para Sim, e "N" para Não: '.format(
                                        SaborPR))
                        if Decisao.lower() == "s":
                                continue

                        elif Decisao.lower() == "n":
                                break
                        else:
                                print('Digite somente S para sim e N para não')
# Duas bolas de sorvete
                elif numeroDeBolasPR == 2:
                        Calculo5 += SaborPR1
                        Decisao = input('\nvocê pediu 2 bolas de sorvete no sabor Premium: R$ {:.2f} \nDeseja mais algum sorvete, digite S "Sim", e N para "Não"'.format(
                                        SaborPR1))
                        if Decisao.lower() == "s":
                                continue

                        elif Decisao.lower() == "n":
                                break
                        else:
                                print('Digite somente Y para sim e N para não')
# Tres bolas de sorvete
                elif numeroDeBolasPR == 3:
                        Calculo6 += SaborPR2
                        Decisao = input('\nvocê pediu 3 bolas de sorvete no sabor Premium: R$ {:.2f} \nDeseja mais algum sorvete, digite S "Sim", e N para "Não"'.format(
                                        SaborPR2))
                        if Decisao.lower() == "s":
                                continue

                        elif Decisao.lower() == "n":
                                break
                        else:
                                print('Digite somente Y para sim e N para não')
                else:
                        print('\nNº de bolas Errado')
                        print('digite um valor entre 1 e 3 bolas de sorvete: \n')
                        continue
# sabor Especial
        elif EscolhaSabor.lower() == 'es':
                Calculo7 += SaborES
                numeroDeBolasES = int(
                        input('Você escolheu sorvete sabor Especial\nEntre com numero de bolas de sorvete desejado (1/2/3): '))
# uma bola de Sorvete
                if numeroDeBolasES == 1:
                        Decisao = input('\nvocê pediu 1 bola de sorvete no sabor Especial: R$ {:.2f} \nDeseja mais algum sorvete, digite "S" para Sim, e "N" para Não: '.format(
                                        SaborES))
                        if Decisao.lower() == "s":

                                continue
                        elif Decisao.lower() == "n":
                                break
                        else:
                                print('Digite somente S para sim e N para não')
# Duas bolas de sorvete
                elif numeroDeBolasES == 2:
                        Calculo8 += SaborES1
                        Decisao = input('\nvocê pediu 2 bolas de sorvete no sabor Especial: R$ {:.2f} \nDeseja mais algum sorvete, digite S "Sim", e N para "Não"'.format(
                                        SaborES1))
                        if Decisao.lower() == "s":
                                continue

                        elif Decisao.lower() == "n":
                                break
                        else:
                                print('Digite somente Y para sim e N para não')
# Tres bolas de sorvete
                elif numeroDeBolasES == 3:
                        Calculo9 += SaborES2
                        Decisao = input('\nvocê pediu 3 bolas de sorvete no sabor Especial: R$ {:.2f} \nDeseja mais algum sorvete, digite S "Sim", e N para "Não"'.format(
                                        SaborES2))
                        if Decisao.lower() == "s":
                                continue

                        elif Decisao.lower() == "n":
                                break
                        else:
                                print('Digite somente Y para sim e N para não')
                else:
                        print('\nNº de bolas Errado')
                        print('digite um valor entre 1 e 3 bolas de sorvete: \n')
                        continue

        else:
                print('Sabor de sorvete invalido. Tente novamente')


#Aqui finaliza o codigo, mostrando a soma dos preços pro cliente.
#SE FICAR O CONSOLE TODO BUGADO, ALTERE O VALOR DO CENTER, ESSE 225 É O TAMANHO DO MEU CONSOLE
print('*'*225)

print("Obrigado pela preferência, o valor total a ser pago é de R${:.2f}".format(Calculo1 + Calculo2 + Calculo3 + Calculo4 + Calculo5 + Calculo6 + Calculo7 + Calculo8 + Calculo9).center(225))

print('*'*225)
print('Volte Sempre'.center(225))
print('Jonathan Santos de Oliveira'.center(225))