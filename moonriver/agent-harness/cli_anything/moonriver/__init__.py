import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def transfer(): click.echo('Moonriver transfer')
@cli.command()
def stake(): click.echo('Moonriver stake')
if __name__ == '__main__': cli()
