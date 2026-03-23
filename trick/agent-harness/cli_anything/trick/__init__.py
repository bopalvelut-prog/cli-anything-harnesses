import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('trick running')
@cli.command()
def start(): click.echo('trick started')
if __name__ == '__main__': cli()
