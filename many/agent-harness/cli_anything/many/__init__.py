import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('many running')
@cli.command()
def start(): click.echo('many started')
if __name__ == '__main__': cli()
