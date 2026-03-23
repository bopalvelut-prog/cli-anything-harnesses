import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('resist running')
@cli.command()
def start(): click.echo('resist started')
if __name__ == '__main__': cli()
