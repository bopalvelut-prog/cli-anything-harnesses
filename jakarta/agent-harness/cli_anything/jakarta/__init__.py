import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jakarta running')
@cli.command()
def start(): click.echo('jakarta started')
if __name__ == '__main__': cli()
