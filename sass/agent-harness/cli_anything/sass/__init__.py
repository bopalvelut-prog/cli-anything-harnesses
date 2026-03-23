import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sass running')
@cli.command()
def start(): click.echo('sass started')
if __name__ == '__main__': cli()
