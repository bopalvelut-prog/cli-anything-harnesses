import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('plate running')
@cli.command()
def start(): click.echo('plate started')
if __name__ == '__main__': cli()
