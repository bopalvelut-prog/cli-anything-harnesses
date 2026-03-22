
from nbformat import v4 as nbformat
import json, click

@click.group()
def cli(): pass

@cli.command()
@click.option('-c', '--cells', default=1)
@click.option('-o', '--output', required=True)
def notebook_new(cells, output):
    nb = nbformat.new_notebook()
    for _ in range(cells):
        nb.cells.append(nbformat.new_code_cell(' '))
    with open(output, 'w') as f:
        nbformat.write(nb, f)
    click.echo(f'Created: {output}')

@cli.command()
@click.argument('notebook')
@click.option('-c', '--code', required=True)
@click.option('-t', '--type', 'cell_type', default='code')
def cell_add(notebook, code, cell_type):
    with open(notebook) as f:
        nb = nbformat.read(f, as_version=4)
    if cell_type == 'code':
        cell = nbformat.new_code_cell(code)
    else:
        cell = nbformat.new_markdown_cell(code)
    nb.cells.append(cell)
    with open(notebook, 'w') as f:
        nbformat.write(nb, f)
    click.echo(f'Added cell')

if __name__ == '__main__':
    cli()
