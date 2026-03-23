import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dog running')
@cli.command()
def start(): click.echo('dog started')
if __name__ == '__main__': cli()
