import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('market running')
@cli.command()
def start(): click.echo('market started')
if __name__ == '__main__': cli()
