import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nod running')
@cli.command()
def start(): click.echo('nod started')
if __name__ == '__main__': cli()
