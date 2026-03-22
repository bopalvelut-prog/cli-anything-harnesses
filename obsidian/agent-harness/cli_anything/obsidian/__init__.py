
import click, os
@click.group()
def cli(): pass
VAULT = os.getenv('OBSIDIAN_VAULT', './vault')
@cli.command()
@click.argument('name')
def new(name):
    path = os.path.join(VAULT, f'{name}.md')
    with open(path, 'w') as f: f.write(f'# {name}\n\n')
    click.echo(f'Created: {path}')
@cli.command()
def notes():
    for f in os.listdir(VAULT):
        if f.endswith('.md'): click.echo(f)
if __name__ == '__main__': cli()
