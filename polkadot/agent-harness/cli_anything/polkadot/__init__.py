import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Polkadot node')
@cli.command()
def relay(): click.echo('Polkadot relay chain')
if __name__ == '__main__': cli()
