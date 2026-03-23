import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cactus running')
@cli.command()
def start(): click.echo('cactus started')
if __name__ == '__main__': cli()
