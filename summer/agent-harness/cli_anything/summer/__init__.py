import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('summer running')
@cli.command()
def start(): click.echo('summer started')
if __name__ == '__main__': cli()
