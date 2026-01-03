import os
import sys
try:
    from .extend import extend
except ImportError:
    from extend import extend


# Pastas a ignorar
IGNORED = {'.git', '.vscode', '__pycache__', '.DS_Store', 'node_modules', '.pytest_cache', '.mypy_cache'}

# Cores ANSI
ROOT_COLOR = '\033[94m'
SUB_COLOR = '\033[92m'
RESET = '\033[0m'
ERROR_COLOR = '\033[91m'


def get_emoji(name, is_dir=False):
    # Retorna emoji ou abreviação
    if is_dir:
        return '📁'
    ext = os.path.splitext(name)[1].lower()
    return extend.get(ext, '📄')


def print_tree(path, prefix="", depth=0):
    # Exibe árvore no terminal com cores e tratamento de erros
    try:
        items = sorted([i for i in os.listdir(path) if not (i.startswith('.') or i in IGNORED)])
    except PermissionError:
        print(f"{ERROR_COLOR}[Sem permissão: {path}]{RESET}")
        return
    except Exception as e:
        print(f"{ERROR_COLOR}[Erro ao ler: {e}]{RESET}")
        return
    
    color = ROOT_COLOR if depth == 0 else SUB_COLOR
    
    for i, item in enumerate(items):
        try:
            item_path = os.path.join(path, item)
            is_dir = os.path.isdir(item_path)
            is_last = i == len(items) - 1
            connector = "└── " if is_last else "├── "
            emoji = get_emoji(item, is_dir)
            print(f"{color}{prefix}{connector}{emoji} {item}{RESET}")
            
            if is_dir:
                new_prefix = prefix + ("    " if is_last else "│   ")
                print_tree(item_path, new_prefix, depth + 1)
        except Exception as e:
            print(f"{color}{prefix}[Erro: {item}]{RESET}")


def build_tree_string(path, prefix="", depth=0):
    # Constrói árvore como string para salvar em arquivo
    lines = []
    try:
        items = sorted([i for i in os.listdir(path) if not (i.startswith('.') or i in IGNORED)])
    except (PermissionError, FileNotFoundError):
        return lines
    
    for i, item in enumerate(items):
        try:
            item_path = os.path.join(path, item)
            is_dir = os.path.isdir(item_path)
            is_last = i == len(items) - 1
            connector = "└── " if is_last else "├── "
            emoji = get_emoji(item, is_dir)
            lines.append(f"{prefix}{connector}{emoji} {item}")
            
            if is_dir:
                new_prefix = prefix + ("    " if is_last else "│   ")
                lines.extend(build_tree_string(item_path, new_prefix, depth + 1))
        except Exception:
            continue
    
    return lines


def view(path):
    # Exibe estrutura de pastas com validações
    if not path or not isinstance(path, str):
        print(f"{ERROR_COLOR}Erro: caminho inválido{RESET}")
        return
    
    if not os.path.exists(path):
        print(f"{ERROR_COLOR}Erro: caminho não existe: {path}{RESET}")
        return
    
    if not os.path.isdir(path):
        print(f"{ERROR_COLOR}Erro: não é um diretório: {path}{RESET}")
        return
    
    try:
        folder_name = os.path.basename(path)
        print(f"{ROOT_COLOR}📂 {folder_name}{RESET}")
        print_tree(path)
        
        if input("Deseja salvar em .md? (s/n): ").lower().strip() == 's':
            md_file = f"{folder_name}_tree.md"
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(f"# Estrutura da pasta {folder_name}\n\n```\n")
                    f.write(f"📂 {folder_name}\n")
                    f.write("\n".join(build_tree_string(path)))
                    f.write("\n```\n")
                print(f"✓ Salvo em {md_file}")
            except IOError as e:
                print(f"{ERROR_COLOR}Erro ao salvar arquivo: {e}{RESET}")
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário.")
    except Exception as e:
        print(f"{ERROR_COLOR}Erro inesperado: {e}{RESET}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        view(sys.argv[1])
    else:
        view("C:\\Users\\marco\\OneDrive\\Documentos\\GitHub\\noctis_map")