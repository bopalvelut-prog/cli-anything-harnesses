import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rs running')
@cli.command()
def start(): click.echo('rs started')
if __name__ == '__main__': cli()
