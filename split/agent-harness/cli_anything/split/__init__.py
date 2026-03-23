import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('split running')
@cli.command()
def start(): click.echo('split started')
if __name__ == '__main__': cli()
