import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stare running')
@cli.command()
def start(): click.echo('stare started')
if __name__ == '__main__': cli()
