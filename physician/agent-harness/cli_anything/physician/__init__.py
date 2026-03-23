import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('physician running')
@cli.command()
def start(): click.echo('physician started')
if __name__ == '__main__': cli()
