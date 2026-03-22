import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def transfer(): click.echo('Shiden transfer')
@cli.command()
def stake(): click.echo('Shiden stake')
if __name__ == '__main__': cli()
