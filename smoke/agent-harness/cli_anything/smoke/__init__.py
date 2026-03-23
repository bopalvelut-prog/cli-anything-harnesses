import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('smoke running')
@cli.command()
def start(): click.echo('smoke started')
if __name__ == '__main__': cli()
