import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('variety running')
@cli.command()
def start(): click.echo('variety started')
if __name__ == '__main__': cli()
