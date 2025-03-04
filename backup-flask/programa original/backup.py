import os
from tkinter.filedialog import askdirectory
import shutil
import datetime

pasta_selecionada = askdirectory()

lista_arquivos = os.listdir(pasta_selecionada)

nome_pasta_backup = "backup"
nome_completo_pasta_backup = os.path.join(pasta_selecionada, nome_pasta_backup)
if not os.path.exists(nome_completo_pasta_backup):
    os.mkdir(nome_completo_pasta_backup)

data_atual = datetime.datetime.today().strftime("%Y-%m-%d_%H%M%S")
pasta_backup_timestamp = os.path.join(nome_completo_pasta_backup, data_atual)

for arquivo in lista_arquivos:
    if arquivo == nome_pasta_backup:
        continue

    nome_completo_arquivo = os.path.join(pasta_selecionada, arquivo)
    nome_final_arquivo = os.path.join(pasta_backup_timestamp, arquivo)

    if os.path.isfile(nome_completo_arquivo):
        dest_dir = os.path.dirname(nome_final_arquivo)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir, exist_ok=True)
        shutil.copy2(nome_completo_arquivo, nome_final_arquivo)
    elif os.path.isdir(nome_completo_arquivo):
        shutil.copytree(nome_completo_arquivo, nome_final_arquivo)