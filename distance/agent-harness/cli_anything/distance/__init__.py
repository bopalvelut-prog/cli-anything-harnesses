import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('distance running')
@cli.command()
def start(): click.echo('distance started')
if __name__ == '__main__': cli()
