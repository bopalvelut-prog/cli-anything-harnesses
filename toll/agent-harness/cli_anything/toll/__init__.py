import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('toll running')
@cli.command()
def start(): click.echo('toll started')
if __name__ == '__main__': cli()
