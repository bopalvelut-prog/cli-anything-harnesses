import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('modular running')
@cli.command()
def start(): click.echo('modular started')
if __name__ == '__main__': cli()
