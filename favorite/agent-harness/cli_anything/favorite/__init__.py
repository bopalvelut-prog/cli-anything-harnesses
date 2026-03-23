import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('favorite running')
@cli.command()
def start(): click.echo('favorite started')
if __name__ == '__main__': cli()
