import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autodesk running')
@cli.command()
def start(): click.echo('autodesk started')
if __name__ == '__main__': cli()
