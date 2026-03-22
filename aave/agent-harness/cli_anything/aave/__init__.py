import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def supply(): click.echo('Aave supply')
@cli.command()
def borrow(): click.echo('Aave borrow')
if __name__ == '__main__': cli()
