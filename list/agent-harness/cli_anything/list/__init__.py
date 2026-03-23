import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('list running')
@cli.command()
def start(): click.echo('list started')
if __name__ == '__main__': cli()
