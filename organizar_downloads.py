import os
import shutil

# Diretório da pasta de downloads
downloads_dir = r"D:\OneDrive\Downloads"

# Função para mover os arquivos para suas respectivas pastas
def organizar_pasta(downloads_dir):
    # Lista de extensões para os tipos de arquivos
    tipos_arquivos = {
        'PDF': '.pdf',
        'Vídeos': ('.mp4', '.mkv', '.avi', '.mov'),
        'Músicas': ('.mp3', '.wav', '.flac'),
        'Imagens': ('.jpg', '.jpeg', '.png', '.gif'),
        'Documentos': ('.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'),
        'Arquivos_zipados': ('.zip', '.rar', '.tar.gz'),
        'Outros': ()
    }

    # Cria diretórios para cada tipo de arquivo, se não existirem
    for tipo in tipos_arquivos:
        caminho_pasta = os.path.join(downloads_dir, tipo)
        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)

    # Move os arquivos para as respectivas pastas
    for arquivo in os.listdir(downloads_dir):
        caminho_arquivo = os.path.join(downloads_dir, arquivo)
        if os.path.isfile(caminho_arquivo):
            ext = os.path.splitext(arquivo)[1].lower()
            movido = False
            for tipo, extensoes in tipos_arquivos.items():
                if ext in extensoes:
                    destino = os.path.join(downloads_dir, tipo, arquivo)
                    shutil.move(caminho_arquivo, destino)
                    movido = True
                    break
            if not movido:
                destino = os.path.join(downloads_dir, 'Outros', arquivo)
                if not os.path.exists(os.path.join(downloads_dir, 'Outros')):
                    os.makedirs(os.path.join(downloads_dir, 'Outros'))
                shutil.move(caminho_arquivo, destino)

if __name__ == "__main__":
    organizar_pasta(downloads_dir)
    print("Arquivos organizados com sucesso!")
