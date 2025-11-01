from .ide import IDE

def ide(path):
    """
    Função rápida para iniciar o editor IDE com o caminho do arquivo.
    """
    ide_instance = IDE()
    ide_instance.edit(path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        ide(sys.argv[1])
    else:
        print("Uso: python ide_funct.py <arquivo>")