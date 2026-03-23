import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('traverse running')
@cli.command()
def start(): click.echo('traverse started')
if __name__ == '__main__': cli()
