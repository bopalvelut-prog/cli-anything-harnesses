import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('while running')
@cli.command()
def start(): click.echo('while started')
if __name__ == '__main__': cli()
