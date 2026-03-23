import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('balance running')
@cli.command()
def start(): click.echo('balance started')
if __name__ == '__main__': cli()
