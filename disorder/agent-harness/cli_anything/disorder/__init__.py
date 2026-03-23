import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('disorder running')
@cli.command()
def start(): click.echo('disorder started')
if __name__ == '__main__': cli()
