import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Ethereum node')
@cli.command()
def wallet(): click.echo('Ethereum wallet')
if __name__ == '__main__': cli()
