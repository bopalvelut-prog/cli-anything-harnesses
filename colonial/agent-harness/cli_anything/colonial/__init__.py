import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('colonial running')
@cli.command()
def start(): click.echo('colonial started')
if __name__ == '__main__': cli()
