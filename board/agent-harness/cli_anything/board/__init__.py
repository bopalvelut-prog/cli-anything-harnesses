import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('board running')
@cli.command()
def start(): click.echo('board started')
if __name__ == '__main__': cli()
