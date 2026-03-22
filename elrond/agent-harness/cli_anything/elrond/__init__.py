import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def account(): click.echo('Elrond account')
@cli.command()
def transfer(): click.echo('Elrond transfer')
if __name__ == '__main__': cli()
