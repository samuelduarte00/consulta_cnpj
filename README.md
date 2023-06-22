
# Consulta de CNPJ 🕵️

Consulta situação cadastral, CNAE, sócios e outras informações de um CNPJ. Dados públicos disponibilizados pela Receita Federal utilizando API disponibilizada pela [invertexto](https://api.invertexto.com/).
Código feito 100% em Python, utilizando as bibliotecas **tkinter**, para gerar a interface interativa para o código e **requests**, para requisição à API.

Adicionei um widget `Text` chamado `result_text`, que será usado para exibir os dados JSON formatados. Após obter a resposta da API, os dados são formatados usando a função `json.dumps()` com o argumento `indent=4` para fornecer uma formatação legível. Em seguida, os dados formatados são inseridos no widget Text.

Além disso, modifiquei a disposição dos elementos usando o gerenciador de layout `grid` para uma melhor organização.


## Instalação

Instale as bibliotecas requests e tkinter

```bash
  pip install pip install tk
```
```bash
  pip install requests
```    

Gerar o token gratuito para API no site [invertexto](https://api.invertexto.com/):

- [Gerar Token API](https://api.invertexto.com/)


## Código

```python
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

```


## Criando arquivo executável do código

Para criar um arquivo executável a partir do código anterior, foi utilizado a ferramenta PyInstaller. O PyInstaller permite empacotar um script Python e suas dependências em um arquivo executável independente que pode ser executado em um ambiente sem Python instalado.

Aqui estão as etapas básicas para criar um arquivo executável usando o **PyInstaller**:

1. Instale o PyInstaller executando o seguinte comando no terminal:

```bash
  pip install pyinstaller
```

2. Salve o código do script em um arquivo chamado `cnpj.py`

3. No terminal, navegue até o diretório que contém o arquivo `cnpj.py`.

4. Execute o seguinte comando para criar o arquivo executável:

```bash
  pyinstaller pdf_extractor.py --onefile --noconsole
```

Isso irá criar um diretório chamado dist e um arquivo executável dentro dele.

Após a conclusão dessas etapas, você encontrará o arquivo executável na pasta **`dist`**. Você pode distribuir esse arquivo executável para outros usuários, e eles poderão executar o programa sem a necessidade de ter o Python ou quaisquer bibliotecas instaladas.

Observação: O PyInstaller cria um arquivo executável específico para o sistema operacional em que você está executando o comando. Portanto, se você estiver executando o comando no macOS, o executável será específico para macOS. Se você quiser criar executáveis para outros sistemas operacionais, você pode executar o comando em um sistema operacional diferente ou usar ferramentas adicionais, como o **PyInstaller cross-compilation**, para criar executáveis para diferentes sistemas operacionais em uma única máquina.


## Funcionalidades

- Consulta situação cadastral, CNAE, sócios e outras informações de um CNPJ
- Interface simples e interativa
