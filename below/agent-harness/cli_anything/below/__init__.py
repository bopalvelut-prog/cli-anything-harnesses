import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('below running')
@cli.command()
def start(): click.echo('below started')
if __name__ == '__main__': cli()
