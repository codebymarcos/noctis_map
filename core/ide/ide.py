import os
import sys
import pathlib
from prompt_toolkit import PromptSession
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.key_binding import KeyBindings
from pygments.lexers import get_lexer_by_name


class IDE:
    # Editor com realce de sintaxe no terminal
    
    LANGUAGES = {
        '.py': 'python', '.js': 'javascript', '.ts': 'typescript', '.jsx': 'jsx',
        '.tsx': 'typescript', '.java': 'java', '.c': 'c', '.cpp': 'cpp', '.cs': 'csharp',
        '.php': 'php', '.rb': 'ruby', '.go': 'go', '.rs': 'rust', '.swift': 'swift',
        '.html': 'html', '.css': 'css', '.scss': 'scss', '.json': 'json', '.xml': 'xml',
        '.yaml': 'yaml', '.yml': 'yaml', '.md': 'markdown', '.sh': 'bash', '.sql': 'sql',
    }
    
    # Detecta linguagem pela extensão
    def detect_language(self, path):
        ext = pathlib.Path(path).suffix.lower()
        return self.LANGUAGES.get(ext, 'text')
    
    # Carrega arquivo
    def load_file(self, path):
        return [] if not os.path.exists(path) else open(path, 'r', encoding='utf-8').read().splitlines()
    
    # Salva arquivo
    def save_file(self, path, lines):
        with open(path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
    
    # Configura lexer para realce
    def _get_lexer(self, lang):
        try:
            if lang != 'text':
                lex_inst = get_lexer_by_name(lang)
                return PygmentsLexer(lex_inst.__class__)
        except Exception as e:
            print(f"Erro lexer: {e}")
        return None
    
    # Abre arquivo para edição
    def edit(self, path):
        lang = self.detect_language(path)
        content = '\n'.join(self.load_file(path))
        print(f"Linguagem: {lang}")
        
        kb = KeyBindings()
        @kb.add('c-s')
        def save_exit(e):
            e.app.exit(result=e.app.current_buffer.text)
        
        print("Ctrl+S: salvar | Ctrl+D: sair")
        try:
            new_content = PromptSession(lexer=self._get_lexer(lang), multiline=True, key_bindings=kb).prompt("", default=content)
            self.save_file(path, new_content.splitlines())
            print("Salvo!")
        except KeyboardInterrupt:
            print("Cancelado.")
        except EOFError:
            print("Finalizado.")


def main():
    if len(sys.argv) > 1:
        IDE().edit(sys.argv[1])
    else:
        print("Uso: python ide.py <arquivo>")


if __name__ == "__main__":
    main()