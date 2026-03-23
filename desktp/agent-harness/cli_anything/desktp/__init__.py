import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('desktp running')
@cli.command()
def start(): click.echo('desktp started')
if __name__ == '__main__': cli()
