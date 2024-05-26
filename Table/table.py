from rich.console import Console
from rich.table import Table

table = Table()
console = Console()
def dynamic_table_of(rows=[], cols=[], title=''):
    global table
    title = title if title else "Menu"
    table = Table(title=title)

    for col in cols:
        table.add_column(col, style="magenta")
    
    for row in rows:
        table.add_row(*row)
    
    return table

def get_console():
    global console
    return console
