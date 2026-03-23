import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('move running')
@cli.command()
def start(): click.echo('move started')
if __name__ == '__main__': cli()
