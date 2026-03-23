import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('science running')
@cli.command()
def start(): click.echo('science started')
if __name__ == '__main__': cli()
