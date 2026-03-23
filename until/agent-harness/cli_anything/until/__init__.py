import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('until running')
@cli.command()
def start(): click.echo('until started')
if __name__ == '__main__': cli()
