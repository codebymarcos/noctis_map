# CLI para noctis_map - ferramentas de visualização e edição de projetos

import sys
import os
import argparse
from rich.console import Console

# Adiciona diretório pai ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from commands import scan, view, ide
from art import get_logo

console = Console()

VERSION = "1.0.0"


def show_help():
    # Banner usando componente de arte
    console.print(get_logo(), highlight=False)
    console.print(f"[dim]v{VERSION} - Ferramentas para análise e edição de projetos[/dim]\n")
    
    # Comandos estilo cargo
    console.print("[bold white]USAGE:[/bold white]")
    console.print("    ntc [green]<command>[/green] [cyan]<args>[/cyan]\n")
    
    console.print("[bold white]COMMANDS:[/bold white]")
    console.print("    [green]scan[/green]    Escaneia pasta e gera markdown com conteúdo")
    console.print("    [green]view[/green]    Visualiza estrutura em árvore colorida")
    console.print("    [green]ide[/green]     Editor terminal com realce de sintaxe\n")
    
    console.print("[bold white]EXAMPLES:[/bold white]")
    console.print("    [dim]$[/dim] ntc scan ./projeto")
    console.print("    [dim]$[/dim] ntc view .")
    console.print("    [dim]$[/dim] ntc ide main.py\n")
    
    console.print("[bold white]OPTIONS:[/bold white]")
    console.print("    [cyan]-h, --help[/cyan]      Mostra esta ajuda")
    console.print("    [cyan]-v, --version[/cyan]   Mostra a versão")


def main():
    # Verifica flags especiais
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-v', '--version']:
            console.print(f"[bold green]noctis[/bold green] v{VERSION}")
            return
        if sys.argv[1] in ['-h', '--help']:
            show_help()
            return
    
    parser = argparse.ArgumentParser(
        prog='ntc',
        description='Ferramentas para análise e edição de projetos',
        add_help=False
    )
    
    subparsers = parser.add_subparsers(dest='command')
    
    # Registra comandos
    scan.register(subparsers)
    view.register(subparsers)
    ide.register(subparsers)
    
    args = parser.parse_args()
    
    if not args.command:
        show_help()
        return
    
    try:
        args.func(args)
        console.print("\n[bold green]+[/bold green] [green]Concluído com sucesso![/green]")
    except KeyboardInterrupt:
        console.print("\n[yellow]-[/yellow] [yellow]Operação cancelada pelo usuário[/yellow]")
        sys.exit(130)
    except Exception as e:
        console.print(f"\n[bold red]x error:[/bold red] {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
