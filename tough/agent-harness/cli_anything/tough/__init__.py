import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tough running')
@cli.command()
def start(): click.echo('tough started')
if __name__ == '__main__': cli()
