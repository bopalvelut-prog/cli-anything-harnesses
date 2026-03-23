import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('surely running')
@cli.command()
def start(): click.echo('surely started')
if __name__ == '__main__': cli()
