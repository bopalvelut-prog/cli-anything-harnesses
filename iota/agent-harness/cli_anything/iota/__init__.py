import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('IOTA node')
@cli.command()
def transfer(): click.echo('IOTA transfer')
if __name__ == '__main__': cli()
