import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Aptos node')
@cli.command()
def account(): click.echo('Aptos account')
if __name__ == '__main__': cli()
