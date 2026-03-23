import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('harm running')
@cli.command()
def start(): click.echo('harm started')
if __name__ == '__main__': cli()
