"""import tkinter

def clique():
    print("Fazer Login")

janela = tkinter.Tk()
janela.geometry("500x300")
texto = tkinter.Label(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

botao = tkinter.Button(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)
janela.mainloop()"""

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def clique():
    print("Fazer Login")

janela = customtkinter.CTk()
janela.geometry("500x300")

texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar Login")
checkbox.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela,text="Login", command=clique)
botao.pack(padx=10, pady=10)


janela.mainloop()