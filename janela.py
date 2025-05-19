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

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.geometry("500x300")
        self.title("Tela de Login")

        self.texto = customtkinter.CTkLabel(self, text="Fazer Login")
        self.texto.pack(padx=10, pady=10)

        self.email = customtkinter.CTkEntry(self, placeholder_text="Seu e-mail")
        self.email.pack(padx=10, pady=10)

        self.senha = customtkinter.CTkEntry(self, placeholder_text="Sua senha", show="*")
        self.senha.pack(padx=10, pady=10)

        self.checkbox = customtkinter.CTkCheckBox(self, text="Lembrar Login")
        self.checkbox.pack(padx=10, pady=10)

        self.botao = customtkinter.CTkButton(self, text="Login", command=self.clique)
        self.botao.pack(padx=10, pady=10)

    def clique(self):
        print("Fazer Login")

app = App()
app.mainloop()