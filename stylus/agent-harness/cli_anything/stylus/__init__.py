import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stylus running')
@cli.command()
def start(): click.echo('stylus started')
if __name__ == '__main__': cli()
