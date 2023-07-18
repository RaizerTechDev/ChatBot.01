# Importar os
# pip3 install pyinstaller
import os


def processar_resposta(resposta, nome):
    if resposta == "1":
        print(
            f"{os.linesep}{nome} A média salarial de um programador Python é em torno de R$ 150.000,00 por ano.{os.linesep}"
        )
    elif resposta == "2":
        print(
            # vai acrescentar ao os.linesep => que significa linha separação ou seja ir para linha de baixo.
            f"{os.linesep}{nome} Vale muito a pena aprender Python, pois é uma das linguagens que mais cresce atualmente.{os.linesep}"
        )

    elif resposta == "3":
        print(
            f"{os.linesep}{nome} para se tornar um desenvolvedor de python você precisa estudar alguns temas que são muito relevantes para a profissão.\nÉ preciso se dedicar e estar sempre em busca de novos conhecimentos.\nUma boa forma de aprimorar seus conhecimentos e aprender muita coisa interessante, é através dos cursos como a (Stackx, Dio, Udemy, Nerd dos Dados entre outras) e assim ficar por dentro das novas techs.{os.linesep}"
        )
    else:
        print("Digite apenas as opções 1, 2 ou 3")


def start():
    # Apresentar o chatbot
    print("Olá, Bem vindo ao bot, sou (desenvolvedor rafarz76dev!)")

    # Pedir o nome
    nome = input("\nQual é seu nome: ")

    while True:
        # Oferecer um menu de opções e vai acrescentar ao os.linesep => que significa linha separação ou seja ir para linha de baixo.
        resposta = input(
            f"\nO que gostaria de saber hoje {nome}? {os.linesep}\n[1] - A média salarial de um profissional que trabalha com Python?{os.linesep}[2] - Se vale a pena aprender Python?  {os.linesep}[3] - Ou como eu faço pra me tornar um Desenvolvedor em Python?\n{os.linesep}"
        )

        # Processar a resposta enviada
        processar_resposta(resposta, nome)


if __name__ == "__main__":
    start()
