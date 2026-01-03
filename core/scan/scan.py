import os
import sys
import pathlib


# Extensões a ignorar
IGNORED_EXTENSIONS = {
    '.exe', '.dll', '.so', '.dylib', '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2',
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.ico', '.svg',
    '.mp3', '.mp4', '.avi', '.mkv', '.wav', '.flac',
    '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'
}


def scan(path):
    # Escaneia arquivos e cria markdown com conteúdo
    folder_name = os.path.basename(os.path.normpath(path))
    output_file = f"{folder_name}.md"
    
    with open(output_file, 'w', encoding='utf-8') as md:
        md.write(f"# Conteúdo da pasta {folder_name}\n\n")
        
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                ext = pathlib.Path(file_path).suffix.lower()
                
                if ext in IGNORED_EXTENSIONS:
                    continue
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    rel_path = os.path.relpath(file_path, path)
                    md.write(f"## {rel_path}\n\n```\n{content}\n```\n\n")
                except (UnicodeDecodeError, PermissionError):
                    continue


if __name__ == "__main__":
    if len(sys.argv) > 1:
        scan(sys.argv[1])
    else:
        scan("C:\\Users\\marco\\OneDrive\\Documentos\\GitHub\\noctis_map\\core")