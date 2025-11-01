import os
from .extend import extend

def view(path):
    # mostrar a estrutura de pastas e arquivos de um diretório como uma árvore

    #ignorar pastas ocultas .git .vscode __pycache__ etc

    # adicionar emojis para extençoes de arquivos, e pastas

    # printar no terminal

    # perguntar se quer salvar em um arquivo .md
    
    ignored_names = {'.git', '.vscode', '__pycache__', '.DS_Store', 'node_modules', '.pytest_cache', '.mypy_cache'}
    
    # Cores ANSI
    root_color = '\033[94m'  # Azul para raiz
    sub_color = '\033[92m'   # Verde para subpastas
    reset = '\033[0m'
    
    def get_emoji(name, is_dir=False):
        if is_dir:
            return '📁'
        ext = os.path.splitext(name)[1].lower()
        return extend.get(ext, '📄')
    
    def print_tree(current_path, prefix="", depth=0):
        items = sorted(os.listdir(current_path))
        filtered_items = [item for item in items if not (item.startswith('.') or item in ignored_names)]
        color = root_color if depth == 0 else sub_color
        for i, item in enumerate(filtered_items):
            item_path = os.path.join(current_path, item)
            is_last = i == len(filtered_items) - 1
            connector = "└── " if is_last else "├── "
            emoji = get_emoji(item, os.path.isdir(item_path))
            print(f"{color}{prefix}{connector}{emoji} {item}{reset}")
            if os.path.isdir(item_path):
                new_prefix = prefix + ("    " if is_last else "│   ")
                print_tree(item_path, new_prefix, depth + 1)
    
    def build_tree_string(current_path, prefix="", depth=0):
        lines = []
        items = sorted(os.listdir(current_path))
        filtered_items = [item for item in items if not (item.startswith('.') or item in ignored_names)]
        for i, item in enumerate(filtered_items):
            item_path = os.path.join(current_path, item)
            is_last = i == len(filtered_items) - 1
            connector = "└── " if is_last else "├── "
            emoji = get_emoji(item, os.path.isdir(item_path))
            lines.append(f"{prefix}{connector}{emoji} {item}")
            if os.path.isdir(item_path):
                new_prefix = prefix + ("    " if is_last else "│   ")
                lines.extend(build_tree_string(item_path, new_prefix, depth + 1))
        return lines
    
    print(f"{root_color}📂 {os.path.basename(path)}{reset}")
    print_tree(path)
    
    save = input("Deseja salvar em um arquivo .md? (s/n): ").lower().strip()
    if save == 's':
        folder_name = os.path.basename(path)
        md_file = f"{folder_name}_tree.md"
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(f"# Estrutura da pasta {folder_name}\n\n")
            f.write("```\n")
            f.write(f"📂 {os.path.basename(path)}\n")
            tree_lines = build_tree_string(path)
            f.write("\n".join(tree_lines))
            f.write("\n```\n")
        print(f"Salvo em {md_file}")

if __name__ == "__main__":
    view("C:\\Users\\marco\\Documents\\GitHub\\noctis_map")