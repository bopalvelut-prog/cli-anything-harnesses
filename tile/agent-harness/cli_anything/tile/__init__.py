import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tile running')
@cli.command()
def start(): click.echo('tile started')
if __name__ == '__main__': cli()
