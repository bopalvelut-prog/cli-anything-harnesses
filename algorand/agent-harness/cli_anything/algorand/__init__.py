import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Algorand node')
@cli.command()
def account(): click.echo('Algorand account')
if __name__ == '__main__': cli()
