import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('training running')
@cli.command()
def start(): click.echo('training started')
if __name__ == '__main__': cli()
