import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Avalanche node')
@cli.command()
def subnet(): click.echo('Avalanche subnet')
if __name__ == '__main__': cli()
