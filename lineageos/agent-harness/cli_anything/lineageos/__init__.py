import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lineageos running')
@cli.command()
def start(): click.echo('lineageos started')
if __name__ == '__main__': cli()
