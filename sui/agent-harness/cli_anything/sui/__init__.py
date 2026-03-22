import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Sui node')
@cli.command()
def account(): click.echo('Sui account')
if __name__ == '__main__': cli()
