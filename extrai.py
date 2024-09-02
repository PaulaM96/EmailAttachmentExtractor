import os
import zipfile
import extract_msg
import tkinter as tk
from tkinter import messagebox

# Caminho da pasta onde estão os e-mails
caminho_pasta = r"\\caminho"
# Pasta de destino para os arquivos extraídos
caminho_extraidos = os.path.join(caminho_pasta, "ARQUIVOS_EXTRAIDOS")

# Cria a pasta de extração se não existir
os.makedirs(caminho_extraidos, exist_ok=True)

def extrair_anexos_msg(caminho_arquivo):
    """Extrai anexos de arquivos .msg e extrai os ZIPs contidos neles."""
    try:
        msg = extract_msg.Message(caminho_arquivo)
        msg.attachments  # Carrega os anexos

        # Percorre os anexos do e-mail
        for attachment in msg.attachments:
            filename = attachment.longFilename

            if filename.lower().endswith('.zip'):
                caminho_zip = os.path.join(caminho_extraidos, filename)

                # Salva o arquivo ZIP
                with open(caminho_zip, 'wb') as zip_file:
                    zip_file.write(attachment.data)

                # Extrai os arquivos do ZIP
                with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                    zip_ref.extractall(caminho_extraidos)

    except Exception as e:
        print(f"Erro ao processar o arquivo {caminho_arquivo}: {e}")

def processar_pasta(caminho):
    """Percorre todos os arquivos na pasta e processa os e-mails."""
    for root, dirs, files in os.walk(caminho):
        for file in files:
            if file.lower().endswith('.msg'):  # Verifica se o arquivo é do tipo .msg
                caminho_arquivo = os.path.join(root, file)
                extrair_anexos_msg(caminho_arquivo)

def extrair_emails():
    """Função chamada pelo botão para iniciar a extração."""
    processar_pasta(caminho_pasta)
    messagebox.showinfo("Concluído", f"Arquivos dos e-mails salvos na pasta: {caminho_extraidos}")

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Extrator de Anexos de E-mails")

# Configuração do botão
botao_extrair = tk.Button(janela, text="Extrair E-mail", command=extrair_emails, padx=20, pady=10)
botao_extrair.pack(pady=20)

# Inicia o loop da interface gráfica
janela.mainloop()
