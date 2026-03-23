import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nkn running')
@cli.command()
def start(): click.echo('nkn started')
if __name__ == '__main__': cli()
