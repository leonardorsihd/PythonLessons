import getpass
import msvcrt

usuarios= {
    "Victor": "080404", "Pedro" : "123456", "Ingrid": "100504", "higor": "123456"}


def login():
    username = input("nome de usuario ")
    password = ""
    print("Digite sua senha:") 

    while True:
        caractere = msvcrt.getch().decode('utf-8')

        if caractere == "\r": 
            break

        password += caractere
        print("*", end='', flush=True) 

    

    if username in usuarios and usuarios[username] == password:
        print("Login bem-sucedido!")
    else:
        print("Nome de usuário ou senha incorretos.") 
  



login()