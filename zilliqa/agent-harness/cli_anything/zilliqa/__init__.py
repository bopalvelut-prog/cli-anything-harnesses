import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def account(): click.echo('Zilliqa account')
@cli.command()
def transfer(): click.echo('Zilliqa transfer')
if __name__ == '__main__': cli()
