import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('military running')
@cli.command()
def start(): click.echo('military started')
if __name__ == '__main__': cli()
