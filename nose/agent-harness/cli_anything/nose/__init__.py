import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nose running')
@cli.command()
def start(): click.echo('nose started')
if __name__ == '__main__': cli()
