import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def account(): click.echo('Qtum account')
@cli.command()
def transfer(): click.echo('Qtum transfer')
if __name__ == '__main__': cli()
