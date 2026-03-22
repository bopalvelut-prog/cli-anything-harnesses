import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def server(): subprocess.run(['hugo', 'server'])
@cli.command()
def build(): subprocess.run(['hugo'])
@cli.command()
@click.argument('name')
def new(name): subprocess.run(['hugo', 'new', 'site', name])
if __name__ == '__main__': cli()
