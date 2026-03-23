import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hear running')
@cli.command()
def start(): click.echo('hear started')
if __name__ == '__main__': cli()
