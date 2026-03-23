import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scale running')
@cli.command()
def start(): click.echo('scale started')
if __name__ == '__main__': cli()
