import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def supply(): click.echo('Compound supply')
@cli.command()
def borrow(): click.echo('Compound borrow')
if __name__ == '__main__': cli()
