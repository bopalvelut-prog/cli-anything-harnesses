import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('photo running')
@cli.command()
def start(): click.echo('photo started')
if __name__ == '__main__': cli()
