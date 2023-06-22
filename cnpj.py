import requests
import tkinter as tk
from tkinter import messagebox
import json


def obter_dados_cnpj():
    cnpj = cnpj_entry.get()
    link = "https://api.invertexto.com/v1/cnpj/" + cnpj + \
        "?token=TOKEN" #Adicionar o token aqui!

    req = requests.get(link)

    if req.status_code == 200:
        result = req.json()
        formatted_result = json.dumps(result, indent=4)

        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, formatted_result)
    else:
        messagebox.showerror(
            "Erro", "Não foi possível obter os dados do CNPJ.")


# Criar a janela principal
window = tk.Tk()
window.title("Consulta CNPJ")

# Criar os elementos da interface
cnpj_label = tk.Label(window, text="CNPJ:")
cnpj_entry = tk.Entry(window)
consultar_button = tk.Button(
    window, text="Consultar", command=obter_dados_cnpj)
result_text = tk.Text(window, height=20, width=80)

# Posicionar os elementos na janela
cnpj_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
cnpj_entry.grid(row=0, column=1, padx=10, pady=10)
consultar_button.grid(row=0, column=2, padx=10, pady=10)
result_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Iniciar o loop principal da janela
window.mainloop()