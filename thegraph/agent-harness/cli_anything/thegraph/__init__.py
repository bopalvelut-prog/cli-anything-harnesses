import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def query(): click.echo('The Graph query')
@cli.command()
def deploy(): click.echo('The Graph deploy')
if __name__ == '__main__': cli()
