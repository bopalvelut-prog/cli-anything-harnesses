import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('escape running')
@cli.command()
def start(): click.echo('escape started')
if __name__ == '__main__': cli()
