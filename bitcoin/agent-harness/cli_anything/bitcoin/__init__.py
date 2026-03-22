import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Bitcoin node')
@cli.command()
def wallet(): click.echo('Bitcoin wallet')
if __name__ == '__main__': cli()
