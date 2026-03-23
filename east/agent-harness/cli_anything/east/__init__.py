import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('east running')
@cli.command()
def start(): click.echo('east started')
if __name__ == '__main__': cli()
