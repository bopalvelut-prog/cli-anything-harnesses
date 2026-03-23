import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('half running')
@cli.command()
def start(): click.echo('half started')
if __name__ == '__main__': cli()
