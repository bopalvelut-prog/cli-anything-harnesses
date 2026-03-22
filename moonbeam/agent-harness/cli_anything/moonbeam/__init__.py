import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def transfer(): click.echo('Moonbeam transfer')
@cli.command()
def stake(): click.echo('Moonbeam stake')
if __name__ == '__main__': cli()
