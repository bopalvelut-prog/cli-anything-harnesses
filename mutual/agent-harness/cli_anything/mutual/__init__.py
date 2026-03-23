import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mutual running')
@cli.command()
def start(): click.echo('mutual started')
if __name__ == '__main__': cli()
