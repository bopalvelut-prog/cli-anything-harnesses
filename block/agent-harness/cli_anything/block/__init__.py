import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('block running')
@cli.command()
def start(): click.echo('block started')
if __name__ == '__main__': cli()
