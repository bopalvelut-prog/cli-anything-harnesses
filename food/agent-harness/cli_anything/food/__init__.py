import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('food running')
@cli.command()
def start(): click.echo('food started')
if __name__ == '__main__': cli()
