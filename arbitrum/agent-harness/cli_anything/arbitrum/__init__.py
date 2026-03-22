import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Arbitrum node')
@cli.command()
def bridge(): click.echo('Arbitrum bridge')
if __name__ == '__main__': cli()
