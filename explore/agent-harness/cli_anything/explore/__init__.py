import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('explore running')
@cli.command()
def start(): click.echo('explore started')
if __name__ == '__main__': cli()
