import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cayley running')
@cli.command()
def start(): click.echo('cayley started')
if __name__ == '__main__': cli()
