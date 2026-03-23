import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('promote running')
@cli.command()
def start(): click.echo('promote started')
if __name__ == '__main__': cli()
