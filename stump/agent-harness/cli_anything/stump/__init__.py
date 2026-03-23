import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stump running')
@cli.command()
def start(): click.echo('stump started')
if __name__ == '__main__': cli()
