import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Moralis started')
@cli.command()
def query(): click.echo('Moralis query')
if __name__ == '__main__': cli()
