import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tin running')
@cli.command()
def start(): click.echo('tin started')
if __name__ == '__main__': cli()
