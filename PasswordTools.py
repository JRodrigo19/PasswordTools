#import tkinter as tk
#from tkinter import messagebox
import random
import string

special_c = "@!#$%¨&*()-=+_"

def gerar_senha(l_pass, u_pass, d_pass, s_pass):
    password = []

    password += random.choices(string.ascii_lowercase, k=l_pass)
    password += random.choices(string.ascii_uppercase, k=u_pass)
    password += random.choices(string.digits, k=d_pass)
    password += random.choices(special_c, k=s_pass)

    random.shuffle(password)

    return ''.join(password)

def verificar_condições(prompt):
    valor = input(prompt)
    if not valor.isdigit():
        print(f"\nNada foi digitado ou o que foi digitado não é um número!")
    valor = int(valor)
    if valor < 1:
        print(f"\nO número digitado precisa ser maior que 0!")
    return valor

try:
    while True:

        lower_pass = verificar_condições("\nDigite quantas letras minúsculas a senha terá: ")
        upper_pass = verificar_condições("\nDigite quantas letras maiúsculas a senha terá: ")
        digit_pass = verificar_condições("\nDigite quantos números a senha terá: ")
        special_pass = verificar_condições("\nDigite quantos caracteres especiais a senha terá: ")

        #Soma todas as variáveis
        soma_total = lower_pass + upper_pass + digit_pass + special_pass

        #Verifica se a soma de todas as variáveis é igual ou menor que 12
        if(soma_total < 12):
            print("O tamanho da senha não corresponde ao mínimo recomendado de 12 caracteres")
        else:
            senha_gerada = gerar_senha(lower_pass, upper_pass, digit_pass, special_pass)
            print(f"\nSenha gerada: {senha_gerada}")

        sair = input("\nDigite exit para sair ou pressione enter para continuar: ")
        if(sair.lower() == 'exit'):
            break

except Exception as e:
    print(f"erro: {e}")





