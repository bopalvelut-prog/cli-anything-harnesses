import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Celestia node')
@cli.command()
def light(): click.echo('Celestia light client')
if __name__ == '__main__': cli()
