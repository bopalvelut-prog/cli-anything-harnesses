import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reload running')
@cli.command()
def start(): click.echo('reload started')
if __name__ == '__main__': cli()
