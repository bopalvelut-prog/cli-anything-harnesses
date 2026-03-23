import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stair running')
@cli.command()
def start(): click.echo('stair started')
if __name__ == '__main__': cli()
