import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def account(): click.echo('Hedera account')
@cli.command()
def transfer(): click.echo('Hedera transfer')
if __name__ == '__main__': cli()
