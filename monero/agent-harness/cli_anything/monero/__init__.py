import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Monero node')
@cli.command()
def wallet(): click.echo('Monero wallet')
if __name__ == '__main__': cli()
