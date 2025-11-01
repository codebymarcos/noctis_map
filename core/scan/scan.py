import os
import pathlib

def scan(path):
    # escanear todos os arquivos da pasta
    
    # ignorar executaveis zipados e etc

    # criar um arquivo <nome da pasta>.md com todo o conteudo de todos os arquivos
    
    # Extensões a ignorar (executáveis, zipados e outros binários comuns)
    ignored_extensions = {
        '.exe', '.dll', '.so', '.dylib', '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2',
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.ico', '.svg',
        '.mp3', '.mp4', '.avi', '.mkv', '.wav', '.flac',
        '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'
    }
    
    folder_name = os.path.basename(os.path.normpath(path))
    output_file = f"{folder_name}.md"
    
    with open(output_file, 'w', encoding='utf-8') as md_file:
        md_file.write(f"# Conteúdo da pasta {folder_name}\n\n")
        
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                ext = pathlib.Path(file_path).suffix.lower()
                
                if ext in ignored_extensions:
                    continue
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    relative_path = os.path.relpath(file_path, path)
                    md_file.write(f"## {relative_path}\n\n")
                    md_file.write("```\n")
                    md_file.write(content)
                    md_file.write("\n```\n\n")
                except (UnicodeDecodeError, PermissionError):
                    # Pular arquivos que não podem ser lidos como texto
                    continue

if __name__ == "__main__":
    scaner = scan("C:\\Users\\marco\\Documents\\GitHub\\noctis_map\\core")