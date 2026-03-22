import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def transfer(): click.echo('Klaytn transfer')
@cli.command()
def stake(): click.echo('Klaytn stake')
if __name__ == '__main__': cli()
