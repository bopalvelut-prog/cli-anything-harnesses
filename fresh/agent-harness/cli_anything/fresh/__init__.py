import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fresh running')
@cli.command()
def start(): click.echo('fresh started')
if __name__ == '__main__': cli()
