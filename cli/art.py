# Componente de arte ASCII para noctis_map

from rich.console import Console

console = Console()

LOGO = """
[bold yellow]       *    .    +    *    .[/bold yellow]
[bold cyan]███╗   ██╗ ██████╗  ██████╗████████╗██╗███████╗[/bold cyan]
[bold cyan]████╗  ██║██╔═══██╗██╔════╝╚══██╔══╝██║██╔════╝[/bold cyan]
[bold green]██╔██╗ ██║██║   ██║██║        ██║   ██║███████╗[/bold green]
[bold green]██║╚██╗██║██║   ██║██║        ██║   ██║╚════██║[/bold green]
[bold blue]██║ ╚████║╚██████╔╝╚██████╗   ██║   ██║███████║[/bold blue]
[bold blue]╚═╝  ╚═══╝ ╚═════╝  ╚═════╝   ╚═╝   ╚═╝╚══════╝[/bold blue]
[bold yellow]          +        .    *[/bold yellow]
"""

def show_logo():
    console.print(LOGO, highlight=False)

def get_logo():
    return LOGO
