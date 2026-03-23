import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('anymatch running')
@cli.command()
def start(): click.echo('anymatch started')
if __name__ == '__main__': cli()
