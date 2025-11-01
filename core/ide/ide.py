import os
import pathlib
from prompt_toolkit import PromptSession
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.key_binding import KeyBindings
from pygments.lexers import get_lexer_by_name

class IDE:
    # input do arquivo a editar
    
    # detectar o tipo de arquivo e linguagem

    # abrir arquivo no terminal para edição

    # usar a lib rich para destacar a sintaxe de acordo com a linguagem

    # ctrl+s para salvar e voltar ao terminal
    
    def __init__(self):
        self.language_map = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.html': 'html',
            '.css': 'css',
            '.json': 'json',
            '.md': 'markdown',
            '.sh': 'bash',
            '.sql': 'sql',
            '.xml': 'xml',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            # Add more as needed
        }
    
    def detect_language(self, file_path):
        ext = pathlib.Path(file_path).suffix.lower()
        return self.language_map.get(ext, 'text')
    
    def load_file(self, file_path):
        if not os.path.exists(file_path):
            return []
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().splitlines()
    
    def save_file(self, file_path, lines):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
    
    def edit(self, file_path):
        language = self.detect_language(file_path)
        lines = self.load_file(file_path)
        content = '\n'.join(lines)
        
        print(f"Linguagem detectada: {language}")
        
        try:
            pygments_lexer = get_lexer_by_name(language)
            lexer = PygmentsLexer(pygments_lexer())
        except Exception as e:
            print(f"Erro no lexer: {e}")
            lexer = None
        
        kb = KeyBindings()
        
        @kb.add('c-s')
        def save_and_exit(event):
            event.app.exit(result=event.app.current_buffer.text)
        
        session = PromptSession(lexer=lexer, multiline=True, key_bindings=kb)
        print("Editando o arquivo. Pressione Ctrl+S para salvar e sair, ou Ctrl+D.")
        try:
            new_content = session.prompt("", default=content)
            new_lines = new_content.splitlines()
            self.save_file(file_path, new_lines)
            print("Arquivo salvo!")
        except KeyboardInterrupt:
            print("Edição cancelada.")
        except EOFError:
            print("Edição finalizada.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        ide = IDE()
        ide.edit(sys.argv[1])
    else:
        print("Uso: python ide.py <arquivo>")